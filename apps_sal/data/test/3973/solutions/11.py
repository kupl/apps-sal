def main():
    n, m = map(int, input().split())
    a = list(map(lambda x: int(x) - 1, input().split()))
    event = [[] for _ in [0] * m]
    for j, i in enumerate(a):
        if j < n - 1:
            A = m - a[j + 1]
            if A < m:
                event[A].append((True, j))
        B = m - i
        if B < m:
            event[B].append((False, j))
    leader = 1
    now = a[-1]
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            leader += 1
            now += a[i]
    s = a[0]
    ans = 10**20
    for i in range(m):
        for e, j in event[i]:
            if e:
                leader += 1
                now += ((a[j] + i) % m)
            else:
                now -= m
                if j != n - 1:
                    leader -= 1
        now += leader
        ans = min(ans, now - 1 - (s + i) % m)
    print(ans)


main()
