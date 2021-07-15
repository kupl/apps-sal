n = int(input())
c1 = [int(x) for x in input().split()]
c2 = [int(x) for x in input().split()]
c3 = [int(x) for x in input().split()]
c = {'1':c1, '2':c2, '3':c3}

a = {i:[] for i in range(1, n+1)}
for i in range(n-1):
    x, y = [int(x) for x in input().split()]
    a[x].append(y)
    a[y].append(x)

start = 0
bad = False
for k, v in a.items():
    l = len(v)
    if l > 2:
        bad = True
        break
    elif l == 1:
        start = k

if bad:
    print(-1)
else:
    prev = start
    cur = a[start][0]
    b = [prev]
    while True:
       b.append(cur)
       if len(a[cur]) == 1:
           break
       nxt = [x for x in a[cur] if x != prev][0]
       prev = cur
       cur = nxt
    
    ms = sum(c1)+sum(c2)+sum(c3)
    best_per = ''
    for per in {'123', '132', '231', '213', '312', '321'}:
        s = 0
        ci = 0
        for cur in b:
            cvet = per[ci]
            s += c[cvet][cur-1]
            ci = (ci+1)%3
        if s < ms:
            ms = s
            best_per = per

##    print(b)
    print(ms)
    ci = 0
    res = ['' for i in range(n+1)]
    for cur in b:
        cvet = best_per[ci]
        res[cur] = cvet
        ci = (ci+1) % 3
    for i in range(1, n+1):
        print(res[i],end = " ")
    

