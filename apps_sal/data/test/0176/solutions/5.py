def f(a, b, k):
    if a == 0:
        res = b // k + 1
    else:
        res = b // k - (a - 1) // k
    return res


k, a, b = [int(i) for i in input().split()]
if b <= 0:
    res = f(-b, -a, k)
elif a < 0:
    res = f(1, -a, k) + f(0, b, k)
else:
    res = f(a, b, k)
print(res)
