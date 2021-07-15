def prod(li, MOD):
    ret = 1
    for a in li:
        ret *= a
        ret %= MOD
    return ret

N, K = list(map(int, input().split()))
MOD = 1_000_000_007
aaa = list(map(int, input().split()))
if N == K:
    print((prod(aaa, MOD)))
    return
aaa.sort(key=lambda x : abs(x))
if sum(a < 0 for a in aaa[-K:]) % 2 == 0:
    print((prod(aaa[-K:], MOD)))
else:
    if all(a <= 0 for a in aaa):
        bbb = aaa[:K]
    else:
        try:
            x1, y1 = min([a for a in aaa[-K:] if a > 0]), min([a for a in aaa[:-K] if a < 0])
        except:
            x1, y1 = 1, 0
        try:
            x2, y2 = max([a for a in aaa[-K:] if a < 0]), max([a for a in aaa[:-K] if a >= 0])
        except:
            x2, y2 = 1, 0
        bbb = aaa[-K:]
        if abs(x2 * y1) > abs(x1 * y2):
            bbb.remove(x1)
            bbb.append(y1)
        else:
            bbb.remove(x2)
            bbb.append(y2)
    print((prod(bbb, MOD)))

