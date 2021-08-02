N = int(input())
P = list([int(x) - 1 for x in input().split()])
pos = {P[i]: i for i in range(N)}
cur = 0
ans = []
for i in range(N):
    if pos[i] == i:
        continue
    start = pos[i]
    for j in range(start, cur, -1):
        ans.append(j)
        pos[P[j]], pos[P[j - 1]] = pos[P[j - 1]], pos[P[j]]
        P[j], P[j - 1] = P[j - 1], P[j]
    cur = max(cur, start)
if all(i == P[i] for i in range(N)) and cur == N - 1:
    print(("\n".join(map(str, ans))))
else:
    print((-1))
