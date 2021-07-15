from sys import stdin
import numpy as np
def main():
    #入力
    readline=stdin.readline
    mod=10**9+7
    s=readline().strip()
    n=len(s)

    convert=[[0]*13 for i in range(13)]
    for a in range(13):
        for b in range(10):
            convert[a][(10*a+b)%13]=1

    convert=np.array(convert,dtype=np.int64)
    dp=np.zeros(13,dtype=np.int64)
    dp[0]=1
    for i in range(n):
        if s[i]=="?":
            tmp=np.dot(dp,convert)
        else:
            x=int(s[i])
            tmp=np.zeros(13,dtype=np.int64)
            for j in range(13):
                tmp[(j*10+x)%13]=dp[j]
        tmp%=mod
        dp=tmp

    print(dp[5])
    
def __starting_point():
    main()
__starting_point()
