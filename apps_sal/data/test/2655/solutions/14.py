N = int(input())
A = list(map(int, input().split()))

A.sort()
ans = 0
for i in range(N - 1):
    ans += A[N - 1 - (i + 1) // 2]
print(ans)
