n=int(input())
a=list(map(int,input().split()))
totneg=0
tot=0
zero=0
for i in a:
    if i<0:
        if i==0:zero=1
        totneg+=1
        tot+=abs(i)-1
    elif i==0:
        zero=1
        totneg+=1
        tot+=1
    else:
        tot+=i-1
if totneg%2:
    if zero:
        print(tot)
    else:print(tot+2)
else:print(tot)
