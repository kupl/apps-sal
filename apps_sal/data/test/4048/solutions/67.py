N=int(input())
import math
K=math.sqrt(N)
K=round(K)
for i in range(K):
    L=N//K
    if N==L*K:
        break
    else:
        K-=1
ans=K+L
ans-=2
print(ans)
