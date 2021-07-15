def main():
    n, k, q = list(map(int, input().split()))
    l, res = [0] * 200002, []
    for _ in range(n):
        a, b = list(map(int, input().split()))
        l[a] += 1
        l[b + 1] -= 1
    a = 0
    for i, b in enumerate(l):
        a += b
        l[i] = a >= k
    a = 0
    for i, b in enumerate(l):
        if b:
            a += 1
        l[i] = a
    for _ in range(q):
        a, b = list(map(int, input().split()))
        res.append(l[b] - l[a - 1])
    print('\n'.join(map(str, res)))


def __starting_point():
    main()

__starting_point()
