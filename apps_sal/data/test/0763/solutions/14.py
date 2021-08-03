n = int(input())
a = [int(s) for s in input().split()]
mn = float('inf')
for i in range(1, n + 1):
    sum = 0
    for j in range(n):
        sum += a[j] * (abs(j + 1 - i) + j + i - 1) * 2
    mn = min(mn, sum)
print(mn)
