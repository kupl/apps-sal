hh, dd = list(map(int, input().split(':')))

cnt = 0

while True:
    H = str(hh)
    D = str(dd)
    if len(H) < 2:
        H = "0" + H
    if len(D) < 2:
        D = "0" + D
    if H == D[::-1]:
        print(cnt)
        return
    dd += 1
    if dd > 59:
        dd = 0
        hh += 1
    if hh > 23:
        hh = 0
    cnt += 1
