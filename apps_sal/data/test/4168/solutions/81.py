n = int(input())

dp =[0]*40

if n ==0:
    print(0)

elif n >0:
    x = bin(n)
    bx = x[2:]
    lx = len(bx)
    for i in range(lx-1,-1,-1):
        dp[i] = int(bx[lx-1-i])
    for i in range(40):
        if i % 2 ==1 and dp[i]==1:
            dp[i+1] +=1
    while max(dp) >1:
        for i in range(40):
            if dp[i] >=2:
                dp[i] -=2
                if dp[i+1] >0:
                    dp[i+1] -=1
                else:
                    dp[i+1] +=1
                    dp[i+2] +=1
    dpr = list(reversed(dp))
    dprs = list(map(lambda x :str(x),dpr))
    dprj = "".join(dprs)
    print(int(dprj))    

else:
    x = bin(-n)
    bx = x[2:]
    lx = len(bx)
    for i in range(lx-1,-1,-1):
        dp[i] = int(bx[lx-1-i])
    for i in range(40):
        if i % 2 ==0 and dp[i]==1:
            dp[i+1] +=1
    while max(dp) >1:
        for i in range(40):
            if dp[i] >=2:
                dp[i] -=2
                if dp[i+1] >0:
                    dp[i+1] -=1
                else:
                    dp[i+1] +=1
                    dp[i+2] +=1
    dpr = list(reversed(dp))
    dprs = list(map(lambda x :str(x),dpr))
    dprj = "".join(dprs)
    print(int(dprj))    
