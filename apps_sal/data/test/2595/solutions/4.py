from math import ceil
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    bia = bin(a)[2:]
    bib = bin(b)[2:]
    aa = bia.strip('0')
    sca = len(bia) - len(aa)
    bb = bib.strip('0')
    scb = len(bib) - len(bb)
    if aa != bb:
        print(-1)
    else:
        print(ceil(abs(sca - scb) / 3))
