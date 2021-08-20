(a, b, w, x, c) = list(map(int, input().split()))
poc = 0
s = set()
s.add(b)
(pa, pb, pc) = (a, b, c)
while c > a:
    c -= 1
    if b >= x:
        b = b - x
    else:
        a -= 1
        b = w - (x - b)
    if b in s:
        kolko = len(s)
        break
    s.add(b)
dl = len(s)
kolko = max(pa - a, 1)
if dl == kolko:
    print(0)
else:
    roz = (pc - pa) // (dl - kolko) - 1
    poc = roz * dl
    c = pc - poc
    a = pa - roz * kolko
    b = pb
    while c > a:
        c -= 1
        if b >= x:
            b = b - x
        else:
            a -= 1
            b = w - (x - b)
        poc += 1
    print(poc)
