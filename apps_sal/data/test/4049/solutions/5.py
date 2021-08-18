import math
for _ in range(1):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mi = 0
    ar, ass, ap = a[0], a[1], a[2]
    br, bss, bp = b[0], b[1], b[2]
    ar = max(ar - br, 0)
    ass = max(ass - bss, 0)
    ap = max(ap - bp, 0)

    rock = min(ar, bp)
    ar -= rock
    bp -= rock
    paper = min(ap, bss)
    ap -= paper
    bss -= paper

    sci = min(ass, br)
    ass -= sci
    br -= sci
    mi = ar + ass + ap

    ma = 0
    ar, ass, ap = a[0], a[1], a[2]
    br, bss, bp = b[0], b[1], b[2]
    rock = min(ar, bss)
    ar -= rock
    bss -= rock
    paper = min(ap, br)
    ap -= paper
    br -= paper

    sci = min(ass, bp)
    ass -= sci
    bp -= sci
    ma = rock + paper + sci
    print(mi, ma)
