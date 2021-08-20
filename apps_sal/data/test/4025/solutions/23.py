(a, b, c) = (int(i) for i in input().split())
j = min(a // 3, min(b // 2, c // 2))
a = a - j * 3
b = b - j * 2
c = c - j * 2
G = [1, 2, 3, 1, 3, 2, 1]
ma = 0
for i in range(7):
    (a1, b1, c1) = (a, b, c)
    s = 0
    for h in range(7):
        if G[h] == 1:
            if a1:
                a1 -= 1
            else:
                break
        elif G[h] == 2:
            if b1:
                b1 -= 1
            else:
                break
        elif c1:
            c1 -= 1
        else:
            break
        s += 1
    if s > ma:
        ma = s
    v = G[0]
    del G[0]
    G.append(v)
print(j * 7 + ma)
