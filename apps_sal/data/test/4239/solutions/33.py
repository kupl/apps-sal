def getval():
    n = int(input())
    return n

def main(n):
    dp = [0]
    arr = [1]
    a1 = 6
    a2 = 9
    for i in range(1,100):
        if a1**i<=n:
            arr.append(a1**i)
        else:
            break
    for i in range(1,100):
        if a2**i<=n:
            arr.append(a2**i)
        else:
            break
    arr.sort()
    
    for i in range(1,n+1):
        temp = i 
        for j in arr:
            if j>i:
                break
            temp = min(temp,dp[i-j]+1)
        dp.append(temp)

    print(dp[n])

def __starting_point():
    n = getval()
    main(n)
__starting_point()
