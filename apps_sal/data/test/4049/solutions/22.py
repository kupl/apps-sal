import itertools
n = int(input())
(a1, a2, a3) = map(int, input().split())
(b1, b2, b3) = map(int, input().split())
win = min(a1, b2) + min(a2, b3) + min(a3, b1)
mx = 0
pt = -1
mx = 0
for lists in itertools.permutations(range(6)):
    ct = 0
    aa1 = a1
    aa2 = a2
    aa3 = a3
    bb1 = b1
    bb2 = b2
    bb3 = b3
    for pt in lists:
        L = [min(aa1, bb1), min(aa1, bb3), min(aa2, bb1), min(aa2, bb2), min(aa3, bb2), min(aa3, bb3)]
        if pt == 0:
            aa1 -= L[0]
            bb1 -= L[0]
        if pt == 1:
            aa1 -= L[1]
            bb3 -= L[1]
        if pt == 2:
            aa2 -= L[2]
            bb1 -= L[2]
        if pt == 3:
            aa2 -= L[3]
            bb2 -= L[3]
        if pt == 4:
            aa3 -= L[4]
            bb2 -= L[4]
        if pt == 5:
            aa3 -= L[5]
            bb3 -= L[5]
        ct += L[pt]
    if ct > mx:
        mx = ct
print(n - mx, win)
