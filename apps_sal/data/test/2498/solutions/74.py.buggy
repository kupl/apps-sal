from math import gcd


def lcm(a, b):
    return a // gcd(a, b) * b


def lcm(ab):
    l = len(ab)
    ret = ab[0]
    for i in range(1, l):
        ret = ret // gcd(ab[i], ret) * ab[i]
    return ret


def count2(a):
    ret = 0
    while a % 2 == 0:
        a //= 2
        ret += 1
    return 2**ret


n, m = map(int, input().split())
A = list(map(int, input().split()))
if any(i % 2 for i in A):
    print(0)
    return
A = [i // 2 for i in A]
# 全体の最小公倍数
p = lcm(A)
c = count2(p)
# 2で割り切れる回数が同じでないものがある場合
# 違うじゃん
if any(i % c for i in A):
    print(0)
    return
x = m // p
# print(p//c)
if x % 2 == 0:
    print(x // 2)
else:
    print(x // 2 + 1)
