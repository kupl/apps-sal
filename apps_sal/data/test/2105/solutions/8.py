def main():
    (n, m) = list(map(int, input().split()))
    ns = list(input().split())
    ms = list(input().split())
    q = int(input())
    for _ in range(q):
        k = int(input())
        k -= 1
        k1 = k % n
        k2 = k % m
        print(ns[k1] + ms[k2])
    return


def __starting_point():
    main()


__starting_point()
