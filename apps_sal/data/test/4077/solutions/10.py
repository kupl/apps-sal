n,m = map(int,input().split())
a = [int(x) for x in input().split()]

def gC(m,a):
    s = [0 for x in range(2*n + 1)]
    sum = n
    res = 0
    s[sum] = 1
    ad = 0
    for i in range(n):
        if a[i] < m:
            sum -=1
            ad -=s[sum]
        else:
            ad +=s[sum]
            sum +=1
        res +=ad
        s[sum] +=1
    return res


print(gC(m,a) - gC(m + 1,a))
