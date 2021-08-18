a = input().split()
H = int(a[0])
W = int(a[1])
adj = int(0)
s = []
p = []

for k in range(H):
    m = input()
    for i in range(W):
        p.append(m[i])
    s.append(p)
    p = []

for i in range(W):
    i = i - adj
    temp = int(0)
    for k in range(H):
        if s[k][i] == "
        temp = 1
        break
        else:
            pass
    if temp == 0:
        for k in range(H):
            del s[k][i]
        adj += 1
    else:
        pass

W = W - adj
adj = 0

for i in range(H):
    i = i - adj
    temp = int(0)
    for k in range(W):
        if s[i][k] == "
        temp = 1
        break
        else:
            pass
    if temp == 0:
        del s[i]
        adj += 1
    else:
        pass

H = H - adj

for i in range(H):
    tinpo = ''.join(s[i])
    print(tinpo)
