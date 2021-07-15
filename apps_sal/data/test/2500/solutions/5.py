N=int(input())
s=bin(N)[2:]
K=len(s)
mod=10**9+7
#bp[i][j]は上からiビット以上が確定でN>>(K-i)-v>>(K-i)=jとなる通り数
bp=[[0]*(3) for i in range(K+1)]
bp[0][0]=1
for i in range(1,K+1):
    if s[i-1]=="0":
        bp[i][0]=(bp[i-1][1]+bp[i-1][0])%mod
        bp[i][1]=bp[i-1][1]
        bp[i][2]=(bp[i-1][1]+bp[i-1][2]*3)%mod
    else:
        bp[i][0]=bp[i-1][0]
        bp[i][1]=(bp[i-1][1]+bp[i-1][0])%mod
        bp[i][2]=(bp[i-1][1]*2+bp[i-1][2]*3)%mod
print((sum(bp[-1])%mod))

