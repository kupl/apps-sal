from math import gcd
n = int(input())
for i in range(n):
    (a, b) = list(map(int, input().split()))
    if i == 0:
        (pre_a, pre_b) = (a, b)
    if pre_a * b < pre_b * a:
        mul = (pre_b + b - 1) // b
        pre_b = mul * b
        pre_a = pre_b * a // b
    else:
        mul = (pre_a + a - 1) // a
        pre_a = mul * a
        pre_b = pre_a * b // a
print(pre_a + pre_b)
