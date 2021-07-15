# Author:      Divesh Uttamchandani
# Institution: BITS Pilani
n,t = list(map(int,input().strip().split()))
a = list(map(int,input().strip().split()))
s0=0
b = sorted(a, reverse=True)
big = b[0]
s = []
s0=sum(b)
for i in b:
    s.append(s0)
    s0-=i

money=t
ans = 0
for i,total in enumerate(s):
    #print("money left", money)
    #print("ans", ans)
    big1=b[i]
    if(money>=total):
        #print("i can take all max",n-i, total,":", money//total, "times")
        ans+=((n-i)*(money//total))
        money -= total*(money//total)
    #print("ans", ans)
    # now i cannot take all the coins
    # ensure that money goes below big1
    if(money<big1):
        continue
    else:
        while(money>=big1):
            f1 = True
            for ls in range(n):
                if(money-a[ls]>=0):
                    money-=a[ls]
                    #print("adding 1 to ans", big1)
                    f1=False
                    ans+=1
                else:
                    #print("mb",money,big1)
                    pass
                ls+=1
            if(f1==True):
                break
        if(f1==True):
            break


print(ans)
# <> with <3 using Termicoder:
# https://termicoder.github.io

