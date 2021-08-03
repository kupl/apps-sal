import sys
sys.setrecursionlimit(10000000)

n, k = map(int, input().split())
v = list(map(int, input().split()))
ans = 0
for l in range(k + 1):
    for r in range(k - l + 1):
        if l + r > n:
            break

        d = k - l - r
        now = 0
        s = []

        for i in range(l):
            now += v[i]
            s.append(v[i])

        for i in range(n - r, n):
            now += v[i]
            s.append(v[i])

        s.sort()
        for i in range(d):
            if(i >= len(s)):
                break
            if s[i] > 0:
                break

            now -= s[i]

        ans = max(now, ans)
print(ans)
