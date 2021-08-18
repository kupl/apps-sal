m, n = list(map(int, input().split()))
B = [list(map(int, input().split())) for i in range(m)]
sr = [sum(B[i]) for i in range(m)]
sc = [sum([B[i][j] for i in range(m)]) for j in range(n)]
for i in range(m):
    if sr[i] > 0 and sr[i] < n:
        for j in range(n):
            if B[i][j] and sc[j] > 0 and sc[j] < m:
                print('NO')
                return
if sum(sr) > 0 and (max(sr) < n or max(sc) < m):
    print('NO')
else:
    print('YES')
    for i in range(m):
        Ai = [1 if sr[i] == n and sc[j] == m else 0 for j in range(n)]
        print(' '.join(repr(a) for a in Ai))
