n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a.reverse()
a = a + [0] * 100
if sum(a) < m:
    print(-1)
else:
    for ans in range(1, n + 1):
        p = 0
        for i in range((n + ans - 1) // ans):
            for j in range(ans):
                p += max(0, a[i * ans + j] - i)
        if p >= m:
            print(ans)
            break
