from statistics import mean, median, variance, stdev

n = int(input())
A = list(map(int, input().split()))
A_b = A.copy()
for i in range(n):
    tmp = A[i] - i - 1
    A_b[i] = tmp

b = int(median(A_b))

ans = 0
for i in range(n):
    ans += abs(A[i] - b - i - 1)
print(ans)
