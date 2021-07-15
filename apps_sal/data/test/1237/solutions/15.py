n,s=(list(map(int,input().split())))
curtime=0
a=[]
for _ in range(n):
    a.append(tuple(map(int,input().split())))
a.sort()
a.reverse()
for i in a:
    curtime+=max(s-i[0],i[1]-curtime)
    s=i[0]
print(curtime+a[-1][0])

