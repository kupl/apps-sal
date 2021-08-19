(N, W) = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]
w0 = wv[0][0]
wv.sort(key=lambda x: (x[0], -x[1]))
(w1, w2, w3, w4) = ([], [], [], [])
for (w, v) in wv:
    if w == w0:
        w1.append(v)
    elif w == w0 + 1:
        w2.append(v)
    elif w == w0 + 2:
        w3.append(v)
    else:
        w4.append(v)
(Sw1, Sw2, Sw3, Sw4) = ([0], [0], [0], [0])
S = 0
for v in w1:
    S += v
    Sw1.append(S)
S = 0
for v in w2:
    S += v
    Sw2.append(S)
S = 0
for v in w3:
    S += v
    Sw3.append(S)
S = 0
for v in w4:
    S += v
    Sw4.append(S)
(l1, l2, l3, l4) = (len(w1), len(w2), len(w3), len(w4))
V = 0
v = 0
for i in range(l1 + 1):
    if w0 * i > W:
        break
    for j in range(l2 + 1):
        if w0 * i + (w0 + 1) * j > W:
            break
        for k in range(l3 + 1):
            if w0 * i + (w0 + 1) * j + (w0 + 2) * k > W:
                break
            for l in range(l4 + 1):
                if w0 * i + (w0 + 1) * j + (w0 + 2) * k + (w0 + 3) * l > W:
                    break
                v = Sw1[i] + Sw2[j] + Sw3[k] + Sw4[l]
                V = max(V, v)
print(V)
