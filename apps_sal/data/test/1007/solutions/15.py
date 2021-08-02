k, p = map(int, input().split())
z = 9
res = 0
mn = 11
i = 1


def x(i):
    return int(str(i)[::-1])


for i in range(1, k + 1):
    if i < 10:
        res += i * 11
    elif i < 100:
        res += i * 100 + x(i)
    elif i < 10**3:
        res += i * 10**3 + x(i)
    elif i < 10**4:
        res += i * 10**4 + x(i)
    elif i < 10**5:
        res += i * 10**5 + x(i)
    else:
        res += i * 10**6 + x(i)
print(res % p)
