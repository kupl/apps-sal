import math
3
(n, b, p) = [int(i) for i in input().split()]
towels = n * p
bottles = 0


def less_power2(num):
    return 2 ** int(math.log(num, 2))


m = n
while m > 1:
    k = less_power2(m)
    bottles += k * b + k // 2
    m -= k // 2
print(bottles, towels)
