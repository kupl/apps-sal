# ==================================================-
# 最大公約数n個
def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)


def multiple(a, b):
    return a * b // euclid(a, b)


import functools


# ------メイン関数-------
# numsは整数のリスト
def lcm(nums):
    return functools.reduce(multiple, nums)

a=[]

n=int(input())
for i in range(n):
    a.append(int(input()))

print(lcm(a))
