import sys
input = sys.stdin.readline

t = int(input())
ANS = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    ps = [list(map(int, input().split())) for _ in range(m)]
    p = [0] * (n + 1)
    for i in range(m):
        p[ps[i][1]] = max(p[ps[i][1]], ps[i][0])
    for i in range(n)[::-1]:
        p[i] = max(p[i], p[i + 1])
    if p[1] < max(a):
        print(-1)
        continue
    ans = 0
    mx = 0
    cnt = 0
    i = 0
    for x in a:
        cnt += 1
        mx = max(mx, x)
        if p[cnt] < mx:
            ans += 1
            mx = x
            cnt = 1
    if cnt:
        ans += 1
    print(ans)
