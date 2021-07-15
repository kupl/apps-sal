n = int(input())
A = [int(i) for i in input().split()]

ans = 0
S = [0, 0]

for i, a in enumerate(A):
    S[i%2] += a

S[0] -= A[0]
if S[0] == S[1]:
    ans += 1

for i in range(1, n):
    S[i%2] -= A[i]
    S[i%2] += A[i-1]
    if S[0] == S[1]:
        ans += 1

print(ans)
