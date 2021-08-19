N = int(input())
C = []
S = []
F = []
for i in range(N - 1):
    CSF = list(map(int, input().split()))
    C.append(CSF[0])
    S.append(CSF[1])
    F.append(CSF[2])
ans = [0] * N
for i in range(N - 1):
    t = 0
    for j in range(i, N - 1):
        m = -(-t // F[j]) * F[j]
        t = max(S[j], m)
        t += C[j]
    ans[i] = t
print(*ans, sep='\n')
