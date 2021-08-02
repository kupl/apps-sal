for _ in range(int(input())):
    last = {}

    n = int(input())

    a = list(map(int, input().split()))

    nexts = [-1] * n

    for i in range(n - 1, -1, -1):
        if a[i] in last:
            nexts[i] = last[a[i]]

        last[a[i]] = i

    b = 10 ** 6

    for i in range(n):
        if nexts[i] != -1:
            b = min(b, nexts[i] - i + 1)

    print(-1 if b == 10 ** 6 else b)
