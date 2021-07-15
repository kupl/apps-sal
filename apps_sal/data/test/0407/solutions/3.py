n = int(input())
prd = []
adic = {'a':0,'b':1,'c':2,'d':3,'e':4,
            'f':5,'g':6,'h':7,'i':8,'j':9}
fst = [0]*10
for i in range(n):
    raw = list(input())
    fst[adic[raw[0]]]=1
    for i in range(len(raw)):
        prd.append([raw[i],10**(len(raw)-i-1)])
cnt = [0]*10
for i in range(len(prd)):
    k = adic[prd[i][0]]
    cnt[k]+=prd[i][1]
prt = []
p = 1
for i in range(10):
    if fst[i]==1:
        prt.append([i,p])
        p+=1
    else:
        pass
cob = []
for i in range(10):
    cob.append([i,cnt[i],fst[i]])
scob = sorted(cob,key = lambda d:d[1],reverse = True)
p = 1
sum = 0
t = 0
for j in range(10):
    if scob[j][2]==1:
        sum += scob[j][1] * p
        p += 1
    elif scob[j][2]==0 and t == 0:
        t+=1
        pass
    else:
        sum+=scob[j][1]*p
        p+=1
print(sum)
