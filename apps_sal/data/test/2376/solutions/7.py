(N, W) = map(int, input().split())
wv = []
w0 = []
w1 = []
w2 = []
w3 = []
for i in range(N):
    wv.append(list(map(int, input().split())))
wv.sort(key=lambda x: (x[0], -x[1]))
wbase = wv[0][0]
for (w, v) in wv:
    if w == wbase:
        w0.append(v)
    elif w == wbase + 1:
        w1.append(v)
    elif w == wbase + 2:
        w2.append(v)
    else:
        w3.append(v)
(sw0, sw1, sw2, sw3) = ([0], [0], [0], [0])
s = 0
for v in w0:
    s += v
    sw0.append(s)
s = 0
for v in w1:
    s += v
    sw1.append(s)
s = 0
for v in w2:
    s += v
    sw2.append(s)
s = 0
for v in w3:
    s += v
    sw3.append(s)
value = 0
ans = 0
for i in range(len(sw0)):
    if wbase * i > W:
        break
    for j in range(len(sw1)):
        if wbase * i + (wbase + 1) * j > W:
            break
        for k in range(len(sw2)):
            if wbase * i + (wbase + 1) * j + (wbase + 2) * k > W:
                break
            for l in range(len(sw3)):
                if wbase * i + (wbase + 1) * j + (wbase + 2) * k + (wbase + 3) * l > W:
                    break
                value = sw0[i] + sw1[j] + sw2[k] + sw3[l]
                ans = max(ans, value)
print(ans)
