import math
n = int(input())


def eat(k):
    vasya = petya = 0
    candy = n
    while candy > 0:
        ate = 0
        ate = min(candy, k)
        vasya += ate
        candy -= ate
        if candy > 9:
            ate = candy // 10
            petya += ate
            candy -= ate
    return vasya >= petya


l = int(math.log(n, 2))
a = 0
while l >= 0:
    b = 1 << l
    c = n - a - b
    if c > 0 and eat(c):
        a += b
    l -= 1
print(n - a)
