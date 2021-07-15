t = int(input(''))
for _ in range(t):
    n = int(input(''))
    p = list(map(int,input('').split(' ')))
    d = {}
    for i in range(n):
        d[p[i]] = i+1
    exp = [False]*(n+1)
    ans = {}
    for i in range(1,n+1,1):
        if(not exp[i]):
            a = [i]
            c = 1
            t = i
            while(d[t] != i):
                t = d[t]
                exp[t] = True
                c = c+1
                a.append(t)
            for f in a:
                ans[f] = c

    for i in range(1,n+1,1):
        print(ans[i], end = ' ')
    print('')
            
