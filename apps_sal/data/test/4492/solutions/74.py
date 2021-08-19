(N, x) = list(map(int, input().split()))
A = [0] + [int(x) for x in input().split()]
ans = 0
for i in range(1, N + 1):
    if A[i - 1] + A[i] > x:
        ans += A[i - 1] + A[i] - x
        A[i] = x - A[i - 1]
print(ans)
