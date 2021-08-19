(N, M) = map(int, input().split())
ship = [list(map(int, input().split())) for _ in range(M)]
s1 = [False] * N
sN = [False] * N
for (i, s) in enumerate(ship):
    if s[0] == 1:
        s1[s[1] - 1] = True
    if s[1] == N:
        sN[s[0] - 1] = True
ans = 'IMPOSSIBLE'
if any([p1 * pN for (p1, pN) in zip(s1, sN)]):
    ans = 'POSSIBLE'
print(ans)
