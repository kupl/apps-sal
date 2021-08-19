n = int(input())
A = list(map(int, input().split()))
t = max(A)
sums = 0
for j in range(n):
    sums += t - A[j]
print(sums)
