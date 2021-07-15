from sys import stdin
input=stdin.readline
n,m=map(int,input().split())
d = []
for i in range(m):
    d.append(list(map(int,input().split())))
x=d[0][0]
y=d[0][1]
c=[]
e=[]
g=[]
for i in d:
    if x in i:
        c.append(i)
    if y in i:
        e.append(i)
    if x not in i and y not in i:
        g.append(i)
if len(g)==0:
    print('YES');return
s=set(g[0])
for i in g:
    s=s.intersection(set(i))
if len(s)==0:
    print('NO');return
k=list(s)
for s in k:
    fl1=fl2=1
    for i in c:
        if s not in i and y not in i:
            fl1=0
            break
    for i in e:
        if s not in i and x not in i:
            fl2=0
            break
    if fl1 or fl2:
        print('YES');return
print('NO')

