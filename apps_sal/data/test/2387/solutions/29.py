import sys
input = sys.stdin.readline

n=int(input())
s=[input().strip("\n") for _ in range(n)]
p=[];m=[]
for si in s:
    cnt=0;a=0;b=0
    for i in range(len(si)):
        if si[i]==")":
            cnt+=1
        else:
            cnt-=1
        a=max(a,cnt)
    cnt=0
    for i in range(len(si)-1,-1,-1):
        if si[i]=="(":
            cnt+=1
        else:
            cnt-=1
        b=max(b,cnt)
    if b-a>=0:
        p.append((a,si))
    else:
        m.append((-b,si))
p.sort();m.sort()
ss=""

for _,si in p:
    ss+=si
for _,si in m:
    ss+=si
cnt=0
for i in range(len(ss)):
    if ss[i]=="(":
        cnt+=1
    else:
        cnt-=1
    if cnt<0:
        print("No")
        return
if cnt:
    print("No")
else:
    print("Yes")


