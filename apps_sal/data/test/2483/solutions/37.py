N, C = map(int, input().split())
STC = [list(map(int, input().split())) for _ in range(N)]

S = [[] for _ in range(10**5 + 1)]
T = [[] for _ in range(10**5 + 1)]

for s, t, c in STC:
    S[s].append(c)
    T[t].append(c)

used = set()
ans = 0
for i in range(10**5 + 1):
    start = set()
    finish = set()
    for s in S[i]:
        start.add(s)
    for t in T[i]:
        finish.add(t)
    ans = max(ans, len(used) + len(start - finish))
    used = used - finish | start
print(ans)
