def f(m,l):
    tmpm=set()
    for x in m:
        tmpm.add(x+l);tmpm.add(x-l)
    return tmpm

s=input()+"T"
x,y=map(int,input().split())

while s and s[0]=="F":
    x-=1
    s=s[1:]
ss=[{0},{0}]
mode=0
l=0
for i in range(len(s)):
    if s[i]=="F": l+=1
    else:
        ss[mode]=f(ss[mode],l)    
        mode^=1
        l=0

print("Yes" if x in ss[0] and y in ss[1] else "No")
