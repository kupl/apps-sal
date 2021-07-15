def snk_cal(i):
    snk = i
    i = str(i)
    q = 0
    for j in range(len(i)):
        q += int(i[j])
    snk /= q
    return snk

K = int(input())
if K <= 9:
    for i in range(K):
        print((i+1))
else:
    for i in range(9):
        print((i+1))
    K -= 9
    snk = 9
    while K > 0:
        res = snk+1
        d = len(str(res))
        l = []
        for i in range(d):
            n = int(str(res)[:-i-1]+'9'*(i+1))
            l.append(snk_cal(n))
        i = l.index(min(l))
        snk = int(str(res)[:-i-1]+'9'*(i+1))
        print(snk)
        K -= 1

