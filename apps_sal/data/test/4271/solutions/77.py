N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = B[A[0] - 1]
mae = A[0]
for i in range(1, N):
    ans += B[A[i] - 1]
    if A[i] - mae == 1:
        ans += C[mae - 1]
    mae = A[i]
print(ans)
