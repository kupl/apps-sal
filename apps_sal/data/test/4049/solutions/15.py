(n, arr1, arr2) = (int(input()), [int(i) for i in input().split()], [int(i) for i in input().split()])
ma = 0
(a, b) = ([], [])
for i in range(10):
    a.append(arr1)
    b.append(arr2)
ma += min([arr1[0], arr2[1]])
ma += min([arr1[1], arr2[2]])
ma += min([arr1[2], arr2[0]])
mi = n + 1
for x in range(2):
    for y in range(2):
        for z in range(2):
            (aa, bb) = (a[x * 4 + y * 2 + z], b[x * 4 + y * 2 + z])
            (xx, yy, zz) = (min([aa[0], bb[0]]), min([aa[1], bb[1]]), min([aa[2], bb[2]]))
            m = [0] * 10
            if x == 0:
                m[0] -= xx
                m[3] -= xx
            if y == 0:
                m[1] -= yy
                m[4] -= yy
            if z == 0:
                m[2] -= zz
                m[5] -= zz
            (xx, yy, zz) = (min([aa[0] + m[0], bb[2] + m[5]]), min([aa[1] + m[1], bb[0] + m[3]]), min([aa[2] + m[2], bb[1] + m[4]]))
            m[0] -= xx
            m[1] -= yy
            m[2] -= zz
            m[3] -= yy
            m[4] -= zz
            m[5] -= xx
            t = 0
            (xx, yy, zz) = (min([aa[0] + m[0], bb[0] + m[3]]), min([aa[1] + m[1], bb[1] + m[4]]), min([aa[2] + m[2], bb[2] + m[5]]))
            m[0] -= xx
            m[3] -= xx
            m[1] -= yy
            m[4] -= yy
            m[2] -= zz
            m[5] -= zz
            t += min([aa[0] + m[0], bb[1] + m[4]])
            t += min([aa[1] + m[1], bb[2] + m[5]])
            t += min([aa[2] + m[2], bb[0] + m[3]])
            mi = min([mi, t])
print(mi, ma)
