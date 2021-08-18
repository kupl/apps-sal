k, a, b = [int(i) for i in input().split()]
al = [[int(i) for i in input().split()] for j in range(3)]
bb = [[int(i) for i in input().split()] for j in range(3)]
d, sa, sb, cr = dict(), 0, 0, 0
mat = [[(0, 0), (0, 1), (1, 0)],
       [(1, 0), (0, 0), (0, 1)],
       [(0, 1), (1, 0), (0, 0)]]

while cr < k:
    if (a, b) in list(d.keys()):
        break
    cr += 1
    d[(a, b)] = (sa, sb, cr)
    sc = mat[a - 1][b - 1]
    sa += sc[0]
    sb += sc[1]
    a, b = al[a - 1][b - 1], bb[a - 1][b - 1]

if cr == k:
    print(sa, sb)
    return

ln = cr - d[(a, b)][2] + 1
adda = sa - d[(a, b)][0]
addb = sb - d[(a, b)][1]
left = k - cr
cn = left // ln
sa += cn * adda
sb += cn * addb
cr += ln * cn

while cr < k:
    cr += 1
    sc = mat[a - 1][b - 1]
    sa += sc[0]
    sb += sc[1]
    a, b = al[a - 1][b - 1], bb[a - 1][b - 1]

print(sa, sb)
