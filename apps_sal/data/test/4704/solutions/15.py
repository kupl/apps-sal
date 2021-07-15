n = int(input())
A = list(map(int, input().split()))

sum_A = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    sum_A[i] = sum_A[i - 1] + A[i - 1]

ans = float('inf')
for i in range(1, n):
    ans = min(abs(sum_A[i] - (sum_A[-1] - sum_A[i])), ans)
print(ans)
