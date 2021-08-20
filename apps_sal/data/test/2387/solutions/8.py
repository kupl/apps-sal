N = int(input())
S = [input() for i in range(N)]
xs1total = 0
xs2 = []
xs3 = []
xs4total = 0
for s in S:
    n = 0
    m = 0
    for c in s:
        if c == '(':
            n += 1
        elif c == ')':
            n -= 1
            m = min(m, n)
    k = n - m
    if m == 0 and k == 0:
        continue
    elif m == 0:
        xs1total += k
    elif k == 0:
        xs4total += -m
    elif -m < k:
        xs2.append((-m, k))
    else:
        xs3.append((-m, k))
xs2.sort()
xs3.sort(key=lambda x: -x[1])


def check(xs1total, xs2, xs3, xs4total):
    t = xs1total
    for x in xs2:
        if t < x[0]:
            return False
        t = t - x[0] + x[1]
    for x in xs3:
        if t < x[0]:
            return False
        t = t - x[0] + x[1]
    return t == xs4total


if check(xs1total, xs2, xs3, xs4total):
    print('Yes')
else:
    print('No')
