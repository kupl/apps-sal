n, x = list(map(int, input().split()))
a = list(map(int, input().split()))
d = {}
t = {}
ok = False

for i in a:
    try:
        d[i] += 1
    except KeyError:
        d[i] = 1

for i in a:
    if d[i] > 1:
        print(0)
        return
    tmp = x & i

    if tmp != i:
        try:
            t[tmp] += 1
            # if t[tmp] == 2:
            #     ok = True
            #     t[tmp] -= 1
        except KeyError:
            t[tmp] = 1

# print(d)
# print(t)

for i in t:
    try:
        tmp = d[i]
    except KeyError:
        tmp = 0

    if t[i] > 1:
        ok = True
    if t[i] >= 1 and tmp == 1:
        print(1)
        return

if ok:
    print(2)
else:
    print(-1)
