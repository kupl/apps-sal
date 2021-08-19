n = int(input())
a = [int(x) for x in input().rstrip().split()]
now = 1
mod = 10 ** 9 + 7


def lcm(a, b):
    ori_a = a
    ori_b = b
    while b != 0:
        (a, b) = (b, a % b)
    return ori_a * ori_b // a


for i in a:
    now = lcm(i, now)
print(sum([now // i for i in a]) % mod)
