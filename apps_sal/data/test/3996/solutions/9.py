from functools import reduce
mod = 1000000007
n = input()
num = list(map(int, input().split()))
flag = 1 if len(list([x for x in num if x % 2 == 0])) else -1
b = reduce(lambda x, y: pow(x, y, mod), num, 2)
b = b * pow(2, mod - 2, mod) % mod
a = (b + flag) * pow(3, mod - 2, mod) % mod
print("%d/%d" % (a, b))
