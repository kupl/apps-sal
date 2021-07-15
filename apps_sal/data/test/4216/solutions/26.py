n=int(input())
import math
r=math.sqrt(n)
ans=len(str(n))
for i in range(1, math.floor(r)+1):
    if n%i==0:
        ans=min(ans, max(len(str(i)), len(str(n//i))))
print(ans)
