#12 B - Grid Compression
H,W = map(int,input().split())
a = [list(input()) for _ in range(H)]

i = 0
while i < len(a):
    if all(m == '.' for m in a[i]) :
        a.pop(i)
    else:
        i += 1
#加工したaにおけるHを保持しなおす
H_sc = len(a)
w = 0
while w < len(a[0]):
    cnt = 0
    for h in range(H_sc):
        if a[h][w] == '#':
            w += 1
            break
        else:
            cnt += 1
    if cnt == H_sc:
        for b in a:
            b.pop(w)
for g in a:
    print(''.join(g))
