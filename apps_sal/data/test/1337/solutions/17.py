n = int(input())
A = list(map(int, input().split()))

m = int(input())
B = list(map(int, input().split()))
C = list(map(int, input().split()))

D = dict()
for a in A:
    if a not in D:
        D[a] = 1
    else:
        D[a] += 1

P = [0] * m
S = [0] * m
for i in range(m):
    key = B[i]
    if key in D:
        P[i] += D[key]
for i in range(m):
    key = C[i]
    if key in D:
        S[i] += D[key]

ans = 0
for i in range(1, m):
    if P[i] > P[ans] or (P[i] == P[ans] and S[i] > S[ans]):
        ans = i

ans += 1
print(ans)
