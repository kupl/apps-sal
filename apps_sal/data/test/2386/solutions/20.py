N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    A[i] -= i
A.sort()
n = N // 2
ans = 0
for i in range(N):
    ans += abs(A[n] - A[i])
print(ans)
