import collections
n=int(input())
x,v=map(int,input().split())
o=collections.deque()
q=0
k=0
for i in range(1,n):
    s=input()
    if s[0]=='1':
        x,v=map(int,s.split())
        while len(o)>0 and o[-1]<v:
            o.pop()
            k+=1
    if s[0]=='2':
        k+=q
        q=0
    if s[0]=='3':
        x,y=map(int,s.split())
        if v<=y:
            o.append(y)
        else:
            k+=1
    if s[0]=='4':
        q=0
    if s[0]=='5':
        o.clear()
    if s[0]=='6':
        q+=1
print(k)
