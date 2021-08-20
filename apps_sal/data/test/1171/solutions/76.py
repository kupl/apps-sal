def readinput():
    (n, k) = list(map(int, input().split()))
    v = list(map(int, input().split()))
    return (n, k, v)


def main(n, k, v):
    ruisekiL = [0] * (n + 1)
    ruisekiR = [0] * (n + 1)
    for i in range(1, n + 1):
        ruisekiL[i] = ruisekiL[i - 1] + v[i - 1]
        ruisekiR[i] = ruisekiR[i - 1] + v[n - i]
    vv = []
    for i in range(n):
        vv.append((i + 1, v[i]))
    vv.sort(key=lambda x: x[1])
    maxown = -10 ** 7
    for kk in range(k + 1):
        if n < kk:
            own = ruisekiL[n]
            m = 0
            while m < n and vv[m][1] < 0:
                own -= vv[i][1]
                m += 1
            maxown = max(maxown, own)
        else:
            for l in range(kk // 2 + 1):
                for i in range(kk - l + 1):
                    j = kk - i - l
                    jj = n - j + 1
                    own = ruisekiL[i] + ruisekiR[j]
                    m = 0
                    mcnt = 0
                    while mcnt < l:
                        if i < vv[m][0] and vv[m][0] < jj:
                            m += 1
                            continue
                        own -= vv[m][1]
                        mcnt += 1
                        m += 1
                    maxown = max(own, maxown)
    return maxown


def main2(n, k, v):
    ruisekiL = [0] * (n + 1)
    ruisekiR = [0] * (n + 1)
    for i in range(1, n + 1):
        ruisekiL[i] = ruisekiL[i - 1] + v[i - 1]
        ruisekiR[i] = ruisekiR[i - 1] + v[n - i]
    vv = []
    for i in range(n):
        vv.append((i + 1, v[i]))
    vv.sort(key=lambda x: x[1])
    maxown = -10 ** 7
    for i in range(n + 1):
        for j in range(n + 1):
            if i + j > k or i + j > n:
                break
            jj = n - j + 1
            own = ruisekiL[i] + ruisekiR[j]
            l = min(i + j, k - i - j)
            m = 0
            mcnt = 0
            while mcnt < l:
                if i < vv[m][0] and vv[m][0] < jj:
                    m += 1
                    continue
                if vv[m][1] >= 0:
                    break
                own -= vv[m][1]
                mcnt += 1
                m += 1
            maxown = max(own, maxown)
    return maxown


def __starting_point():
    (n, k, v) = readinput()
    ans = main2(n, k, v)
    print(ans)


__starting_point()
