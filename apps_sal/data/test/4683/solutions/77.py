N = int(input())
A = list(map(int, input().split()))
M = 10 ** 9 + 7
Ans = 0
T = sum(A)
for i in range(N - 1):
    T -= A[i]
    Ans += A[i] * T
    Ans %= M
print(Ans)
