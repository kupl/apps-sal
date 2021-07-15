from collections import deque

n, k = map(int, input().split())
v = list(map(int, input().split()))

w = deque(v)
ans = 0
for i in range(k+1):
    if i > n:
        break
    s = v[:i]
    for j in range(k+1-i):
        if j > n-i:
            break
        t = sorted(v[n-j:] + s, reverse=True)
        u = sum(t)
        for l in range(k+1-i-j):
            ans = max(ans, u)
            if not t:
                break
            u -= t.pop()
print(ans)
