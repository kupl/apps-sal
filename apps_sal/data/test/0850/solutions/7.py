
n = int(input())
a = input().split()
ans = ""
cnt = 0
XO = ""
OX = ""
XX = ""

for i in a:
    if i=='100' or i=='0':
        ans += i+" "
        cnt+=1
    else:
        if len(i)==1:
            OX = i
        if len(i)==2:
            if int(i)%10==0:
                XO = i
            else:
                XX = i


if OX=="" and XO=="" and XX!="":
    cnt+=1
    ans+= XX+" "
else:
    if XO!="":
        ans+=XO+" "
        cnt+=1
    if OX!="":
        cnt+=1
        ans+=OX+" "

print(cnt)
print(ans)

