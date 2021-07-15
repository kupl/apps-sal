n,T=map(int,input().split())
a=list(map(int,input().split()))
x=list(map(int,input().split()))
m=[]
q=0
for i in range(n):
    m+=[[x[i],a[i]]]
    q+=a[i]*x[i]
asu=sum(a)
try:
    if q/asu==T:
        print(asu)
    elif q/asu>T:
        m.sort()
        asu-=m[-1][1]
        q-=m[-1][0]*m[-1][1]
        while q/asu>T:
            m.pop()
            asu-=m[-1][1]
            q-=m[-1][0]*m[-1][1]
        print(asu+m[-1][1]*((T*asu-q)/(m[-1][1]*m[-1][0]-T*m[-1][1])))
    else:
        m.sort(reverse=True)
        asu-=m[-1][1]
        q-=m[-1][0]*m[-1][1]
        while q/asu<T:
            m.pop()
            asu-=m[-1][1]
            q-=m[-1][0]*m[-1][1]
        print(asu+m[-1][1]*((T*asu-q)/(m[-1][1]*m[-1][0]-T*m[-1][1])))
except ZeroDivisionError:
    print(0)
