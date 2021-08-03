import math
n = int(input())


def foo(a, b):
    if b == 0:
        return a
    else:
        return foo(b, a % b)


sqrt_n = int(math.sqrt(n)) + 2
res = 0
for i in range(1, sqrt_n):
    for j in range(i, sqrt_n):
        if i * i + j * j > n:
            break
        else:
            d = foo(j * j - i * i, 2 * i * j)
            if d != 1:
                continue
            else:
                res = res + (n // (i * i + j * j))
print(res)
