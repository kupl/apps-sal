n=input()
n=list(input().split())
m=list(input().split())
l=list(input().split())
n.sort()
m.sort()
l.sort()
i=0
while i<len(n):
    if i==len(m):
        q=n[i]
        break
    elif n[i]!=m[i]:
        q=n[i]
        break
    i+=1
i=0
while i<len(m):
    if i==len(l):
        w=m[i]
        break
    elif m[i]!=l[i]:
        w=m[i]
        break
    i+=1
print(q)
print(w)

