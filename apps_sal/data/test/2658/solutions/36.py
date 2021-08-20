(N, K) = map(int, input().split())
A = list(map(int, input().split()))
B = [1]
C = [1] + [0] * (N - 1)
i = 0
while C[A[i] - 1] == 0:
    B.append(A[i])
    C[A[i] - 1] = 1
    i = A[i] - 1
ans = 0
for j in range(len(B)):
    if B[j] == A[i]:
        ans += j
if len(B) - ans != 0 and K - ans > 0:
    ans += (K - ans) % (len(B) - ans)
elif K - ans <= 0:
    ans = K
print(B[ans])
