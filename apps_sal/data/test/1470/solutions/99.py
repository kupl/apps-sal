x=int(input())
from math import ceil
cnt = ceil(x/11)

if 11*cnt - 5 >=x:
    ans=cnt*2-1
else:
    ans=cnt*2
    
print(ans)
