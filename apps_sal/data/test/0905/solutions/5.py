m=list(input().split())
n=int(m[0])
s=int(m[1])*100
m=list()
for i in range(n):
    m.append(list(int(x) for x in input().split()))
t=100000
mi=None
t0=0
for i in range(n):
    if ((m[i][0]*100+m[i][1])<=s and (m[i][1]<t)):
        if m[i][1]:
            t=m[i][1]
        else:
            t0=1
if t==100000:
    if t0:
        print('0')
    else:
        print('-1')
else:
    print(100-t)
        


