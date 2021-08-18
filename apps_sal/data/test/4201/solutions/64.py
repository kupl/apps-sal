import copy


def count(w, h):
    Dtemp = copy.deepcopy(Data)

    for i in range(W):
        if ((1 << i) & w) != 0:
            for hh in range(H):
                Dtemp[hh][i] = 'R'
    for i in range(H):
        if ((1 << i) & h) != 0:
            for ww in range(W):
                Dtemp[i][ww] = 'R'
    c = 0
    for hh in range(H):
        for ww in range(W):
            if Dtemp[hh][ww] == '
            c += 1
    return c


H, W, K = map(int, input().split())
Data = []
for _ in range(H):
    s = input()
    l = []
    for c in s:
        l.append(c)
    Data.append(l)

ans = 0
for w in range(0, 2**W):
    for h in range(0, 2**H):
        if count(w, h) == K:
            ans += 1
print(ans)
