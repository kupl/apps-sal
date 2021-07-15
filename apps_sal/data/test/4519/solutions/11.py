q = int(input())
for __ in [0]*q:
    n,k = list(map(int,input().split()))
    a = list(input())
    q = k
    p = -1
    res = []
    for i in range(n):
        if p == -1 and a[i] == '1':
            p = i
            res.append('1')
        elif p != -1 and a[i] == '0':
            if q >= i-p:
                res[p] = '0'
                res.append('1')
                q -= i-p
                p += 1
            else:
                if q != 0:
                    res[i-q] = '0'
                    res.append('1')
                    q = 0
                else:
                    res.append('0')
        else:
            res.append(a[i])
    ans = ''.join(res)
    print(ans)
        
        
    


