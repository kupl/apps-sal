for t in range(int(input())):
    (p, f) = list(map(int, input().split()))
    (cs, cw) = list(map(int, input().split()))
    (s, w) = list(map(int, input().split()))
    res = 0
    if s > w:
        (s, w) = (w, s)
        (cs, cw) = (cw, cs)
    for ns1 in range(cs + 1):
        if ns1 * s > p:
            continue
        ns2 = min(cs - ns1, f // s)
        nw1 = min((p - ns1 * s) // w, cw)
        nw2 = min((f - ns2 * s) // w, cw - nw1)
        res = max(res, ns1 + ns2 + nw1 + nw2)
    print(res)
