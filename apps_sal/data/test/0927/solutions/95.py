from itertools import combinations_with_replacement
from collections import defaultdict
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))


d = defaultdict(int)  # d[i] = (Aの中でi本用いて表せる最大の数)
for i in range(M):
    if A[i] == 1:
        d[2] = 1
    elif A[i] == 7:
        d[3] = 7
    elif A[i] == 4:
        d[4] = 4
    elif A[i] in [2, 3, 5]:
        d[5] = max(d[5], A[i])
    elif A[i] in [6, 9]:
        d[6] = max(d[6], A[i])
    else:
        d[7] = 8

B = list(d.keys())
B.sort()

a = B[0]
B[0] = 0

if N % a == 0:
    print(''.join([str(d[a])] * (N // a)))
    return


C = []

for i in range(N // a, max(-1, N // a - 7), -1):  # aをi回用いる
    x = N - a * i
    for u in list(combinations_with_replacement(B, 5)):
        if sum(u) == x:
            s = []
            for j in range(5):
                if u[j] != 0:
                    s.append(u[j])
            C.append((i, s))

D = []
for i, j in C:
    if i + len(j) == C[0][0] + len(C[0][1]):
        D.append((i, j))

m = min(D[i][0] for i in range(len(D)))

q, r, s = 0, 0, 0
for i, j in D:
    X = [d[a]] * (i - m) + [d[k] for k in j]
    X.sort(reverse=True)
    M = ''
    for k in X:
        M += str(k)
    M = int(M)
    if q < M:
        q, r, s = M, i, j

E = [d[a]] * r + [d[i] for i in s]
E.sort(reverse=True)

ans = ''
for i in E:
    ans += str(i)
print(ans)
