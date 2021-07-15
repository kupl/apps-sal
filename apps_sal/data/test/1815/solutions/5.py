N = int(input())
A = [int(a) for a in input().split()]

C = [0] * 101010
ma = 0
macnt = 0
poscnt = 0
cntofone = 0
ans = 0
for i in range(N):
    C[A[i]] += 1
    if C[A[i]] > ma:
        ma = C[A[i]]
        macnt = 1
    elif ma == C[A[i]]:
        macnt += 1
    if C[A[i]] == 1:
        poscnt += 1
        cntofone += 1
    elif C[A[i]] == 2:
        cntofone -= 1
    if i <= 1 or (cntofone >= 1 and ((poscnt - 1) * ma == i)) or (macnt == 1 and (poscnt * (ma - 1) == i)):
        ans = i + 1

print(ans)

