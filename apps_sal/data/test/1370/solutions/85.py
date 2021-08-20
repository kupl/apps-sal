(h, w, kk) = list(map(int, input().split()))
s = [list(map(int, list(input()))) for i in range(h)]
l = []
for i in range(2 ** (h - 1)):
    ll = [0]
    for j in range(h - 1):
        if i & 2 ** j:
            ll.append(ll[-1] + 1)
        else:
            ll.append(ll[-1])
    l.append(ll)
mc = w + h
for i in l:
    c = [0 for i in range(h)]
    cc = 0
    f = 1
    for j in range(w):
        ff = 0
        for k in range(h):
            c[i[k]] += s[k][j]
        for k in range(h):
            if c[k] > kk:
                ff = 1
                break
        if ff:
            cc += 1
            c = [0 for i in range(h)]
            for k in range(h):
                c[i[k]] += s[k][j]
            for k in range(h):
                if c[k] > kk:
                    f = 1
            if f:
                cc = w + h
                break
        f = 0
    if mc > cc + len(set(i)) - 1:
        mc = cc + len(set(i)) - 1
print(mc)
