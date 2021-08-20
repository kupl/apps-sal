N = int(input())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7
A_sum = sum(A)
result = 0
for i in range(N):
    A_sum = A_sum - A[i]
    result += A[i] * A_sum % mod
print(result % mod)
