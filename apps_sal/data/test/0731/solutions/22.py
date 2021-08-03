def fhelp(a):
    s = 1
    f = 10
    res = 0
    while a >= s:
        if (a >= s and a < f):
            break
        res += len(str(s)) * k * (f - s)
        s *= 10
        f *= 10
    res += len(str(a)) * k * (a - s + 1)
    return res


def f(a, b):
    return fhelp(b) - fhelp(a - 1)


w, m, k = map(int, input().split())
w += fhelp(m - 1)
# print(fhelp(10))
summ = 0
power = 1
count = 9
while summ <= w:
    q = power * k * count
    if summ + q > w:
        break
    summ += q
    power += 1
    count *= 10
diff = w - summ
diff //= (power * k)
num = 10**(power - 1) + diff
print(num - m)
