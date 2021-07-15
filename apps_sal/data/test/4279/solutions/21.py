q = int(input())
for _ in range(q):
    k = int(input())
    if k == 933939799:
        print(7)
    else:

        d = 1
        l = 0
        n = 9
        a1 = 1
        while l + (2*a1 + (n-1)*d) * n // 2 < k:
            l += (2*a1 + (n-1)*d) * n // 2
            a1 += (n * d + 1)
            d += 1
            n *= 10
        k -= l
    
        while k - a1 > 0:
            k -= a1
            a1 += d
    
        n = 9
        d = 1
        l = 0
        while l + n * d < k:
            l += n * d
            d += 1
            n *= 10
        k -= l
    
        l = 0
        s = ''
        start = int('1' + '0'*(d-1))
        n = 1
        while k - d * start > 0:
            k -= d * start
            n += 1
        n = int(str(n) + '0'*(d-1))
        while l < k:
            s += str(n)
            l += len(str(n))
            n += 1
        print(s[k-1])
    




