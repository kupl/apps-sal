mod = 10 ** 9 + 7
N = int(input())
A = list(map(int, input().split()))
sum_of_all = sum(A) ** 2
sum_of_diagonal = 0
for i in range(N):
    sum_of_diagonal += A[i] ** 2
print((sum_of_all - sum_of_diagonal) // 2 % mod)
