a=int(input())

old=[]
new=[]
d={}
for i in range(a):
    p=input().split()
    old.append(p[0])
    new.append(p[1])
    

dis=[]

for i in range(a):
    if old[i] not in new:
        dis.append(old[i])

print(len(dis))

for i in range(len(dis)):
    p=dis[i]
    q=dis[i]
    for j in range(a):
        if p==old[j]:
            p=new[j]
    s=q+" "+p
    print(s)
