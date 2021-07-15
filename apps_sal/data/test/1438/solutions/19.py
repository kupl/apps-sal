def main():
    from heapq import heapify, heappop, heappushpop
    n, k = list(map(int, input().split()))
    if n == 1:
        a, b = int(input()), int(input())
        print((b + k) // a)
        return
    l = list((b // a, a - (b % a), a) for a, b in zip(list(map(int, input().split())), list(map(int, input().split()))))
    heapify(l)
    b, r, a = heappop(l)
    while k >= r:
        k -= r
        b, r, a = heappushpop(l, (b + 1, a, a))
    print(b)


def __starting_point():
    main()

__starting_point()
