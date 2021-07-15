h, w = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(h)]
def nxtij(i, j):
    if i & 1 == 0:
        if j < w - 1:
            return i, j + 1
        elif i < h - 1:
            return i + 1, j
        else:
            return None
    else:
        if j > 0:
            return i, j - 1
        elif i < h - 1:
            return i + 1, j
        else:
            return None

def ijgen():
    p = 0, 0
    while p:
        yield p
        p = nxtij(*p)
    return
ans = []
for i, j in ijgen():
    if a[i][j] & 1:
        p = nxtij(i, j)
        if p:
            a[p[0]][p[1]] += 1
            ans.append((i+1, j+1, p[0]+1, p[1]+1))
print((len(ans)))
for a in ans:
    print((*a))

