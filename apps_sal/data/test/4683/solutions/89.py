import itertools
n = int(input())
A = list(map(int, input().split()))
A2 = []
for i in range(n):
    A2.append(A[n - 1 - i])

acc_A2 = list(itertools.accumulate(A2))
mod = (10**9) + 7

goukei = 0

for i in range(n - 1):
    goukei += A[i] * acc_A2[n - 2 - i]

print(goukei % mod)
