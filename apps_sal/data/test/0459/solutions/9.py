original = input().split()
original = [int(x) for x in original]


def transform(T, a):
    b = a[:]
    for i in range(0, 24):
        b[T[i]] = a[i]
    return b


def generate_transformation(delta):
    ans0 = [x for x in range(0, 24)]
    ans1 = [x for x in range(0, 24)]
    for (k, v) in delta.items():
        ans0[k - 1] = v - 1
        ans1[v - 1] = k - 1
    return (ans0, ans1)


facegroup = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]


def check_done(facegroup, faces):
    for fg in facegroup:
        for cell in fg:
            if faces[cell - 1] != faces[fg[0] - 1]:
                return False
    return True


tl = {1: 5, 3: 7, 5: 9, 7: 11, 9: 24, 11: 22, 24: 1, 22: 3, 14: 16, 16: 15, 15: 13, 13: 14}
tr = {2: 6, 4: 8, 6: 10, 8: 12, 10: 23, 12: 21, 23: 2, 21: 4, 17: 19, 19: 20, 20: 18, 18: 17}
tt = {13: 5, 14: 6, 5: 17, 6: 18, 17: 21, 18: 2, 21: 13, 22: 14, 1: 3, 3: 4, 4: 2, 2: 1}
td = {15: 7, 16: 8, 7: 19, 8: 20, 19: 23, 20: 24, 23: 15, 24: 16, 9: 10, 10: 12, 12: 11, 11: 9}
tf = {5: 6, 6: 7, 7: 8, 8: 6, 14: 9, 16: 10, 9: 19, 10: 17, 19: 4, 17: 3, 4: 14, 3: 16}
tb = {23: 21, 21: 22, 22: 24, 24: 23, 2: 13, 1: 15, 13: 11, 15: 12, 11: 20, 12: 18, 20: 2, 18: 1}
t = [tl, tr, tt, td, tf, tb]
ok = False
for trans in t:
    (u, v) = generate_transformation(trans)
    if check_done(facegroup, transform(u, original)):
        ok = True
        break
    if check_done(facegroup, transform(v, original)):
        ok = True
        break
if ok:
    print('YES')
else:
    print('NO')
