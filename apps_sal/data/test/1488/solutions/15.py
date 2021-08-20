import math
n = int(input())
l1 = list(map(int, input().split()))
pre_sum = [0]
l1.sort()
for item in l1:
    pre_sum.append(pre_sum[-1] + item)
numerator = 0
for i in range(n):
    numerator += l1[i] * (i + 1) - pre_sum[i] + pre_sum[n] - pre_sum[i + 1] - l1[i] * (n - 1 - i)
y = math.gcd(numerator, n)
print(numerator // y, n // y)
