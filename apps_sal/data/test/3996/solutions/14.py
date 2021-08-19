from functools import reduce
mod = 1000000007
n = input()
num = list(map(int, input().split()))
flag = 1 if len(list(filter(lambda x: x % 2 == 0, num))) else -1
b = reduce(lambda x, y: pow(x, y, mod), num, 2)
b = b * pow(2, mod - 2, mod) % mod  # b = 2^n-1
a = (b + flag) * pow(3, mod - 2, mod) % mod  # a = (2^n-1 -/+ 1) / 3
print("%d/%d" % (a, b))
