N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

A_max = max(A)

M = len(bin(A_max)) - 2
L = len(bin(K)) - 2
C = [[N, 0] for j in range(max(M, L))]
for i in A:
    for j in range(M):
        if (i >> j) & 1:
            C[j][1] += 1
            C[j][0] -= 1

P = 0
for j in range(L-1, -1, -1):
    if C[j][0] >= C[j][1]:
        if P + 2 ** j <= K:
            P += 2 ** j

ans = 0
for i in A:
    ans += P ^ i

print(ans)


