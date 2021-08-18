import sys
N, M = map(int, input().split())
abc = [[] for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    abc[a - 1].append((b - 1, c))

S = [-float("inf")] * N
S[0] = 0
T = [0]
m = 0
n = 0
j = False
while T:
    t = T.pop(0)
    m += 1
    for tb, tc in abc[t]:
        if S[tb] < S[t] + tc:
            S[tb] = S[t] + tc
            T.append(tb)
    if m > M + 1:
        d = abc[tb]
        if N - 1 in list(d[i][0] for i in range(len(d))):
            j = True
        n += 1
    if n > M:
        if j:
            print("inf")
            return
        else:
            break

print(S[-1])
