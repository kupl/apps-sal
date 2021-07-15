from sys import stdin
s=stdin.readline().strip()
x=-1
for i in range(len(s)):
    if s[i]=="[":
        x=i
        break
y=-1
for i in range(len(s)-1,-1,-1):
    if s[i]=="]":
        y=i
        break
if x==-1 or y==-1 or y<x:
    print(-1)
    return
x1=-1
for i in range(x,y):
    if s[i]==":":
        x1=i
        break
y1=-1
for i in range(y-1,x,-1):
    if s[i]==":":
        y1=i
        break
if x1==-1 or y1==-1 or y1<=x1:
    print(-1)
    return
ans=4
for i in range(x1,y1):
    if s[i]=="|":
        ans+=1
print(ans)

