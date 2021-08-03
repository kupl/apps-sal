n = int(input())
n >>= 1
sum1, sum2 = 0, 0
a = list(map(int, input().split()))
a.sort()
for i in range(n):
    sum1 += abs(a[i] - (i * 2 + 1))
    sum2 += abs(a[i] - (i + 1) * 2)
print(min(sum1, sum2))
