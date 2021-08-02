from math import pow
m, n = list(map(int, input().split()))
ans = 0.0
for i in range(1, m + 1):
    ans += i * (pow(i / m, n) - pow((i - 1.0) / m, n))
print('%.15f' % ans)
