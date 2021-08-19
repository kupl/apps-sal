(A, B, C, D) = map(int, input())
tfs = []
rt = str(A)
for bt in (True, False):
    for ct in (True, False):
        for dt in (True, False):
            tfs.append([bt, ct, dt])
for (bt, ct, dt) in tfs:
    tmp = 7 - A
    tmp = tmp - B if bt else tmp + B
    tmp = tmp - C if ct else tmp + C
    tmp = tmp - D if dt else tmp + D
    if tmp == 0:
        rt += '+' if bt else '-'
        rt += str(B)
        rt += '+' if ct else '-'
        rt += str(C)
        rt += '+' if dt else '-'
        rt += str(D)
        rt += '=7'
        break
print(rt)
