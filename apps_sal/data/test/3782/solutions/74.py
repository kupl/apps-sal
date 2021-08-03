N, K, Q = list(map(int, input().split()))
X = list(map(int, input().split()))

r = 10**18
for y in X:
    tmp = []
    tmp2 = []
    for x in X:
        if x < y:
            tmp.sort()
            tn = len(tmp)
            if len(tmp) > K - 1:
                tmp2 += tmp[:tn - K + 1]
            tmp = []
            continue
        tmp.append(x)
    tmp.sort()
    tn = len(tmp)
    if tn - K + 1 > 0:
        tmp2 += tmp[:tn - K + 1]
    tmp2.sort()
    if len(tmp2) >= Q:
        r = min(r, tmp2[Q - 1] - y)
print(r)
