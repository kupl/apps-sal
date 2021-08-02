K = int(input())


def nd(n):
    ans = 0
    nn = n
    while(nn > 0):
        ans += nn % 10
        nn //= 10
    return ans / n


def k_next(k):
    d = 1
    c_max = 0
    ans = k
    while(d < k * 10):
        cand = (k // d + 1) * d + (k % d)
        if nd(cand) >= c_max:
            c_max = nd(cand)
            ans = cand
        d *= 10
    return ans


k = 1
for i in range(K):
    print(k)
    k = k_next(k)
