def sk(k):
    tk = k
    ret = 0
    while tk!=0:
        ret+=tk%10
        tk//=10
    return ret
an = []
for i in range(1,100):
    tp = i/sk(i)
    if len(an)==0:an.append((i,tp))
    else:
        ls=an[-1]
        if ls[1]>tp:an[-1]=(i,tp)
        else:an.append((i,tp))
for j in range(15):
    for i in range(100,1000):
        ns=str(i)+''.join(['9']*j)
        nm=int(ns)
        tp=nm/sk(nm)
        if an[-1][1] > tp:
            while an[-1][1]>tp:
                an.pop()
        an.append((nm,tp))
for i in range(int(input())):print(an[i][0])
