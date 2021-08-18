_ = input()
a = list(map(int, input().split(' ')))
m = input()

res = list()


for _ in range(int(m)):
    w, h = map(int, input().split(' '))
    cmax = max(a[0], a[w - 1])
    res.append(cmax)
    a[0] = cmax + h
    a[w - 1] = cmax + h


print('\n'.join(map(str, res)))
