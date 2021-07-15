def sumto(l):
    n = 1
    o = 1
    e = 2
    S = 0
    i = 0
    par = 0
    t = 0
    while 1:
        par = 1 - par
        t += n
        if t >= l:
            t -= n
            n = l - t
            if par:
                S += n*o + n*(n-1)
                o += 2*n
                n *= 2
            else:
                S += n*e + n*(n-1)
                e += 2*n
                n *= 2
            break
        if par:
            S += n*o + n*(n-1)
            o += 2*n
            n *= 2
        else:
            S += n*e + n*(n-1)
            e += 2*n
            n *= 2
        i += 1
    return S

l,r = list(map(int,input().split()))
mod = 10**9 + 7
print((sumto(r) - sumto(l-1))%mod)

