#E71_C

T = int(input())

for i in range(0, T):
    ln = [int(j) for j in input().split(" ")]
    n = ln[0]
    a = ln[1]
    b = ln[2]
    st = list(input())
    ct = 0
    zct = 0
    pls = 0
    pip = 0
    seg = []
    ft = False
    for j in range(0, len(st)):
        if st[j] == "1":
            ft = False
            if ct == 0:
                seg.append(j - 1)
            ct += 1
            zct = 0
        elif zct == 0 and ct:
            ct += 1
            ft = True
            zct += 1
        else:
            if ft:
                ft = False
                ct -= 1
            zct += 1
            if zct == 2 and ct:
                seg.append(j - 1)
                pls += ct + 1
                zct = 0
                ct = 0
    if zct == 1 and ct:
        seg.append(j)
        if ft:
            ct -= 1
        pls += ct + 1
    cost = pls * (b * 2) + (n + 1 - pls) * (b)
    cost += (n + len(seg)) * a
    if len(seg) > 2:
        for j in range(1, len(seg) - 1,2):
            plc = (seg[j + 1] - seg[j]) * b
            pipc = 2 * a
            if plc < pipc:
                cost -= (pipc - plc)
    print(cost)

