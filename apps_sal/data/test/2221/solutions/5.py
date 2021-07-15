from collections import Counter
x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
x = x1 - x2
y = y1 - y2
xpy = x + y
p2 = (abs(xpy) - 1) // 2
xmy = x - y
m2 = (abs(xmy) - 1) // 2
n = int(input())
s = input().lower()
c = Counter(s)
dr = c['d'] + c['r']
ld = c['l'] + c['d']
lu = c['l'] + c['u']
ru = c['r'] + c['u']


def f(a, b, d, e):
    return a and b // (d if a < 0 else e)


try:
    res = max(f(xpy, p2, ru, ld), f(xmy, m2, dr, lu))
except ZeroDivisionError:
    print('-1')
else:
    dr *= res
    ld *= res
    lu *= res
    ru *= res
    res *= n


    def g(a, b, d, e):
        return a == 0 or (b if a < 0 else d) > e


    for c in s:
        res += 1
        if c in 'dr':
            dr += 1
        if c in 'ld':
            ld += 1
        if c in 'lu':
            lu += 1
        if c in 'ru':
            ru += 1
        if g(xpy, ru, ld, p2) and g(xmy, dr, lu, m2):
            break
    print(res)

