N = int(input())
(*A,) = map(int, input().split())
t = sum(A)
x = 0
ans = float('inf')
for i in range(N - 1):
    x += A[i]
    ans = min(ans, abs(2 * x - t))
print(ans)
