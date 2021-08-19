(N, x) = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(N - 1):
    n = max(0, A[i] + A[i + 1] - x)
    ans += n
    A[i + 1] = max(0, A[i + 1] - n)
print(ans)
