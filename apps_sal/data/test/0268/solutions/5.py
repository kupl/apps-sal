def getIntList():
    return list(map(int, input().split()));
def getTransIntList(n):
    first=getIntList();
    m=len(first);
    result=[[0]*n for _ in range(m)];
    for i in range(m):
        result[i][0]=first[i];
    for j in range(1, n):
        curr=getIntList();
        for i in range(m):
            result[i][j]=curr[i];
    return result;
n, k, d = getIntList()
a= getIntList();
a.sort();
#Возможно разрезать отрезок до j не включительно - cuttable[j];
cuttable=[False]*len(a);
cuttable[0]=True;
def search(a):
    curr=0;
    upLim=0;
    upLimPrev=0;
    while True:
        #print(curr);
        if cuttable[curr]:
            #Добавляем одрезок длины как минимум k: [curr, curr+k)
            lowLim=curr+k;
            upLimPrev = upLim;
            #Находим первый такой индекс upLim, что a[upLim]-a[curr]>d;
            while upLim<len(a) and a[upLim]-a[curr]<=d:
                upLim+=1;
            #Если такого элемента нет, решение найдено
            if upLim==len(a):
                return True;
            #Ставить единички на уже пройденый отрезок бессмысленно
            lowLim=max(lowLim, upLimPrev+1);
            #print('cuttable', lowLim, upLim);
            #a[upLim-1]-a[curr]<=d, значит cuttable[upLim]=True;
            for i in range(lowLim, upLim+1):
                cuttable[i]=True;
        curr+=1;
        if curr>len(a)-k:
            break;
    return False;
if k==1:
    print('YES')
elif search(a):
    print('YES')
else:
    print('NO');
