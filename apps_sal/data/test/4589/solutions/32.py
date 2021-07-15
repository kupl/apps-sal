h,w = map(int, input().split())
sl = []
bl = [["" for _ in range(w)] for _ in range(h)]

for i in range(h):
    s = input()
    sl.append(s)

def scheck(s):
    if s == "#":
        return 1
    else:
        return 0
        
def check(i,j,sl):
    cnt = 0
    for k in range(-1,2):
        for l in range(-1,2):
            if h > i+k >= 0 and w > j+l >= 0:
                cnt += scheck(sl[i+k][j+l])
    return str(cnt)

for i in range(h):
    for j in range(w):
        if sl[i][j] == ".":
            bl[i][j] = check(i,j,sl)
        else:
            bl[i][j] = "#"

for b in bl:
    t = ''.join(b)
    print(t)
