def main():
    n = int(input())
    q = list(map(int, input().split()))
    c = q.copy()
    for i in range(1, n - 1):
        c[i] += c[i - 1]
    q = [0] * n
    q[0] = max(1, 1 - min(c))
    for i in range(1, n):
        q[i] = c[i - 1] + q[0]
    s = set()
    for x in q:
        if x < 1 or x > n or x in s:
            print(-1)
            return
        s.add(x)
    print(*q)


def __starting_point():
    main()


__starting_point()
