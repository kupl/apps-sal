n = int(input())
f = [y for y in map(int, input().split())]

im_f = list(set(f))
ok = True
for y in im_f:
    index = y - 1
    ok &= f[index] == y

if ok:
    m = len(im_f)
    ind = {}
    for i, y in enumerate(im_f):
        ind[y] = i + 1
    print(m)
    values = []
    for y in f:
        values.append(ind[y])
    print(' '.join(map(str, values)))
    print(' '.join(map(str, im_f)))

else:
    print(-1)
