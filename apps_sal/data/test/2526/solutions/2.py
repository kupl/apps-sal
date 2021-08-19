X, Y, A, B, C = [int(n) for n in input().split(" ")]

p = [int(n) for n in input().split(" ")]
q = [int(n) for n in input().split(" ")]
r = [int(n) for n in input().split(" ")]

R = sorted(p)
G = sorted(q)
T = sorted(r)

W = 0
GetR = 0
GetG = 0
GetS = 0

while GetS < X + Y:
    a = -1
    b = -1
    c = -1
    if len(R) > 0 and GetR < X:
        a = R[-1]
    if len(G) > 0 and GetG < Y:
        b = G[-1]
    if len(T) > 0:
        c = T[-1]

    t = max([a, b, c])
    index = [a, b, c].index(t)
    W += t
    #print(R, G, T)
    GetS += 1
    if index == 0:
        del(R[-1])
        GetR += 1
    if index == 1:
        del(G[-1])
        GetG += 1
    if index == 2:
        del(T[-1])

print(W)
