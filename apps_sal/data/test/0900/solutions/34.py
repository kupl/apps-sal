import sys
 
s= sys.stdin.readline().strip()
#
MOD=10**9+7
mmap= []
for i in range(6):
    b = 10**i % 13
    mmap.append( [ [ (b*i+j)%13 for i in range(1,10) ] for j in range(13) ] )
#
dp= [ 0 ] * 13
dp[0] = 1
j= 0
for c in reversed(s):
    tmp = dp.copy()
    #
    if c=="0": pass
    elif c=="?":
        bset = mmap[j]
        for m,num in enumerate(tmp):
            if num==0: continue
            for idx in bset[m]: dp[idx]+=num
        #
        for i in range(13): dp[i]%=MOD
    else:
        b= mmap[j][0][int(c)-1]
        for m in range(13):
            idx= (m+b)%13
            dp[idx]= tmp[m]
    #
    if j==5: j=0
    else: j+=1
#
print((dp[5]))

