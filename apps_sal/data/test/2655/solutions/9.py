N = int(input())
A = list(map(int, input().split()))
A = sorted(A, reverse=True)

ans = 0
for i in range(1, N):
    ans += A[i // 2]
print(ans)
