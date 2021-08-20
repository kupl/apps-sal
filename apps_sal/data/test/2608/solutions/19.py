def fis(sq):
    if sq[2] < sq[0] or sq[3] < sq[1]:
        return [0, 0]
    sc = (sq[0] + sq[1]) % 2
    fc = (sq[2] + sq[3]) % 2
    sxl = sq[2] - sq[0] + 1
    syl = sq[3] - sq[1] + 1
    hf = sxl * syl // 2
    cp = -1
    if sc == fc and (sxl + syl) % 2 == 0 and (sxl % 2 == 1):
        cp = sc
    return [hf + (1 if cp == 0 else 0), hf + (1 if cp == 1 else 0)]


t = int(input())
for i in range(t):
    (n, m) = [int(x) for x in input().split()]
    wco = [int(x) for x in input().split()]
    bco = [int(x) for x in input().split()]
    (wf, bf) = fis([1, 1, m, n])
    btw = fis(wco)[1]
    wtb = fis(bco)[0]
    bnac = [max(wco[0], bco[0]), max(wco[1], bco[1]), min(wco[2], bco[2]), min(wco[3], bco[3])]
    bna = fis(bnac)[1]
    print(wf + btw - wtb - bna, bf + wtb - btw + bna)
