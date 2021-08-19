for _ in range(int(input())):
    (p, f) = list(map(int, input().split()))
    (cs, cw) = list(map(int, input().split()))
    (s, w) = list(map(int, input().split()))
    if w < s:
        (w, s) = (s, w)
        (cs, cw) = (cw, cs)
    ps = p // s
    fs = f // s
    if ps + fs < cs:
        print(ps + fs)
        continue
    best = 0
    for i in range(cs + 1):
        if p < i * s or f < (cs - i) * s:
            continue
        best = max(best, min(cw, (p - i * s) // w + (f - (cs - i) * s) // w) + cs)
    print(best)
