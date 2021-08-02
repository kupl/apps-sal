N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0
cnt = 100
for i in range(N):
    if cnt + 1 == A[i]:
        ans += C[cnt - 1]
    cnt = A[i]
    ans += B[A[i] - 1]

print(ans)
