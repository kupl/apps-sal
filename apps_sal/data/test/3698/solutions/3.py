

def reduce(n):
    n = bin(n)[2:]
    n = list(n)
    n = list(map(int, n))
    return sum(n)


def a(n, bits, dp):
    if(bits == 0):
        return 1

    if(n == '0' or n == ''):
        return 0
    if(bits > len(n)):
        return 0
    if(bits == len(n)):
        if(n == '1' * len(n)):
            # print(n,bits,1)
            return 1
        else:
            return 0
    """
    i=1
    while(i<len(n) and n[i]=='0'):
        i+=1
    
    x=dp[len(n)-1][bits] + a(n[i:],bits-1,dp)
    #print(n,bits,dp[len(n)-1][bits],x)
    return x%1000000007
    """
    ans = 0
    while(bits != 0 and (n != '' and n != '0') and bits < len(n)):
        ans += dp[len(n) - 1][bits]
        i = 1
        while(i < len(n) and n[i] == '0'):
            i += 1
        n = n[i:]
        bits -= 1
    if(bits == 0):
        ans += 1
    elif(bits == len(n) and n == '1' * len(n)):
        ans += 1
    return ans


n = (input())
k = int(input())


if(k > 5):
    print(0)
elif(k == 0):
    print(1)
elif(k == 1):
    print(len(n) - 1)

else:
    dp = []
    dp.append([0, ])
    for i in range(1, 1002):
        dp.append([])

        for j in range(i):
            if(j == 0):
                dp[i].append(1)
            else:
                dp[i].append((dp[i - 1][j - 1] + dp[i - 1][j]) % 1000000007)
        dp[i].append(1)

    pos = []
    for i in range(1, len(n) + 1):
        count = 0
        I = i
        while(i != 1):
            i = reduce(i)
            count += 1
        if(count == k - 1):
            pos.append(I)
    ans = 0
    for i in pos:
        ans += a(n, i, dp)
    # print(dp)
    # print(a('10000',3,dp))

    # print(pos)
    print(ans % 1000000007)
