N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
SA = [0]
SB = [0]
for i in range(len(A)):
    SA.append(SA[i] + A[i])
for j in range(len(B)):
    SB.append(SB[j] + B[j])

l = M
ans = 0
for k in range(N + 1):
    if SA[k] > K:
        break
    while SA[k] + SB[l] > K:
        l -= 1
    ans = max(ans, k + l)
print(ans)
