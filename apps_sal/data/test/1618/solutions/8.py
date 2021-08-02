_ = input()
a = list(map(int, input().split(' ')))
m = input()

res = list()


for _ in range(int(m)):
    w, h = map(int, input().split(' '))
    #print(w, h)
    cmax = max(a[0], a[w - 1])
    res.append(cmax)
    # for x in range(w):
    #     a[x] = cmax + h
    a[0] = cmax + h
    #a[w-1] = cmax + h

    # print(a)

print('\n'.join(map(str, res)))
