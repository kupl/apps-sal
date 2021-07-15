from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n,k=map(int,readline().split())
    a=list(map(int,readline().split()))

    s=bin(max(k,max(a)))[2:]
    l=len(s)
    cnt_one=[0]*l

    for i in range(n):
        b=a[i]
        for j in range(l):
            if b&1==1:
                cnt_one[j]+=1
            b>>=1

    cnt_one.reverse()
    k_bin=bin(k)[2:]
    dp=[[-float("inf"),-float("inf")] for _ in range(l+1)]
    dp[0][0]=0
    for i in range(l):
        j=l-i
        if len(k_bin)<j:
            dp[i+1][0]=dp[i][0]+cnt_one[i]*2**(j-1)
        else:
            if k_bin[len(k_bin)-j]=="1":
                dp[i+1][0]=dp[i][0]+(n-cnt_one[i])*2**(j-1)
                if cnt_one[i]>=(n+1)//2:  #1の数が半数以上
                    dp[i+1][1]=max(dp[i][0]+cnt_one[i]*2**(j-1),dp[i][1]+cnt_one[i]*2**(j-1))
                else:  #1の数が半数未満
                    dp[i+1][1]=max(dp[i][0]+cnt_one[i]*2**(j-1),dp[i][1]+(n-cnt_one[i])*2**(j-1))
            else:
                dp[i+1][0]=dp[i][0]+cnt_one[i]*2**(j-1)
                if cnt_one[i]>=(n+1)//2:  #1の数が半数以上
                    dp[i+1][1]=dp[i][1]+cnt_one[i]*2**(j-1)
                else:  #1の数が半数未満
                    dp[i+1][1]=dp[i][1]+(n-cnt_one[i])*2**(j-1)

    print(max(dp[l][0],dp[l][1]))

def __starting_point():
    main()
__starting_point()
