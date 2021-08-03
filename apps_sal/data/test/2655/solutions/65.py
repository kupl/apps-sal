N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 0
for i in range(N - 1):
    ans += A[N - (i + 1) // 2 - 1]
print(ans)
