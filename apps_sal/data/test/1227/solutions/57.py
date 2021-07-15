# from collections import defaultdict
import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N = int(input())
K = int(input())
keta = len(str(N))
dp = [[0]*(keta) for i in range(4)]
ans = 0

for k in range(1, 4):
    for i in range(1, keta):
        if i<k:
            continue
        else:
            dp[k][i] = comb(i-1, i-k)*(9**k)
#print(dp)
# dp[k][i]: i桁で、k個の0でない数            

ans += sum(dp[K]) # (N の桁)-1 までの累積和

count = 0

for j in range(keta):
    t = int(str(N)[j])
    

    if j==0:
        count+=1
        ans += sum(dp[K-count])*(t-1)
        if count == K: # K==1
            ans+=t
            break
        continue
        
    elif j==keta-1:
        if t!=0:
            count+=1
        if count==K:
            ans+=t
        break
        
        
    if t !=0:
        count+=1
        if count==K:
            ans+=sum(dp[K-count+1][:keta-j]) #0のとき
            ans+=t
            break
        
        ans += sum(dp[K-count][:keta-j])*(t-1)  #0より大きいとき
        ans += sum(dp[K-count+1][:keta-j])   #0のとき
        
   
        
print(ans)
