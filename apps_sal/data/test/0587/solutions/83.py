import sys
input = sys.stdin.readline


N, K = map(int, input().split())
TD = [tuple(map(int, input().split())) for _ in range(N)]

TD.sort(key=lambda x: x[1], reverse=True)

ans = 0
s = set()
r = list()
for i in range(K):
    t, d = TD[i]
    ans += d
    if t not in s:
        s.add(t)
    else:
        r.append(TD[i])
ans += len(s)**2

Ans = ans

for i in range(K, N):
    t0, d0 = TD[i]
    if t0 not in s and len(r) > 0:
        t1, d1 = r.pop()
        ans = ans - d1 + d0 - len(s)**2 + (len(s) + 1)**2
        s.add(t0)
        Ans = max(Ans, ans)

print(Ans)
