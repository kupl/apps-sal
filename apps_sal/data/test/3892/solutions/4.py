def dista(start, n):
    return lambda end: n - (start - end) if(start > end) else end - start

n, m = list(map(int,input().split(' ')))
dicta = [[] for i in range(n+1)]
for i in range(m):
    s, d = list(map(int,input().split(' ')))
    dicta[s].append(d)
for i in range(n+1):
    dicta[i].sort(key = dista(i, n))
maxlen = max((list(map(len, dicta))))


result = (maxlen-1)*n
minadd = 0

ansans = []
for k in range(1, n+1):
    disk = dista(k, n)
    minadd = 0
    for i in range(1, n+1):
        lndicta = len(dicta[i])
        tmp = 0
        if(lndicta == maxlen-1):
            if lndicta != 0:
                tmp = min([(disk(i) + dista(i, n)(j)) for j in dicta[i]]) - n
        elif(lndicta == maxlen):
            tmp = min([(disk(i) + dista(i, n)(j)) for j in dicta[i]])
        if(tmp > minadd):
            minadd = tmp
    ansans.append(str(minadd + result))

print(' '.join(ansans))

