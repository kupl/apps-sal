(n, m) = map(int, input().split())
mass = list(map(int, input().split()))
lr = []
for t in range(m):
    (l, r) = map(int, input().split())
    lr.append([l, r])
mq = 0
mdel = []
mitog = 0
for a in range(len(mass)):
    ma = mass[a]
    for b in range(len(mass)):
        mb = mass[b]
        q = 0
        delete = []
        itog = 0
        for x in range(len(lr)):
            (l, r) = (lr[x][0], lr[x][1])
            if l <= b + 1 <= r and (a + 1 < l or a + 1 > r):
                q += 1
                delete.append(x + 1)
        itog = ma + q - mb
        if mitog < itog:
            mitog = itog
            mq = q
            mdel = delete
print(mitog)
print(mq)
if len(mdel):
    print(' '.join(list(map(str, mdel))))
else:
    print('')
