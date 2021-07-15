K, N = list(map(int, input().split()))
A = list(map(int, input().split()))

a = 0
if A[0] == 0:
    a = K - A[N - 1]
else:
    a = min(A[N - 1] - A[0], K - A[N - 1] + A[0])


for i in range(N - 1):
    b = A[i + 1] - A[i]
    a = max(a, b)
ans = K - a
print(ans)
