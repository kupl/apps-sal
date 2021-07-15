import sys
N, M = map(int, input().split())
P = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
#P = [list(map(int, input().split())) for _ in range(M)]
idx = P[0][0]
S = set()
for i, (a, b) in enumerate(P):
    if a == idx or b == idx:
        continue
    break
else:
    print('YES')
    return
S = set([P[i][0], P[i][1]])
for a, b in P[i:]:
    if a == idx or b == idx:
        continue
    S.intersection_update(set([a, b]))
    if not S:
        break
else:
    print('YES')
    return
idx = P[0][1]
S = set()
for i, (a, b) in enumerate(P):
    if a == idx or b == idx:
        continue
    break
else:
    print('YES')
    return
S = set([P[i][0], P[i][1]])
for a, b in P[i:]:
    if a == idx or b == idx:
        continue
    S.intersection_update(set([a, b]))
    if not S:
        break
else:
    print('YES')
    return
print('NO')
