t = int(input())
for i in range(t):
    a, b, c = sorted(map(int, input().split()))
    res = 10 ** 100
    for p in range(-1, 2):
        for q in range(-1, 2):
            for r in range(-1, 2):
                aa = a + p
                bb = b + q
                cc = c + r
                tmp = abs(aa - bb)
                tmp += abs(aa - cc)
                tmp += abs(cc - bb)
                res = min(res, tmp)
    print(res)
