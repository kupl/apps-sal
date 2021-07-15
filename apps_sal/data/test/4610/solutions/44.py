n,k = map(int,input().split())
from collections import Counter
s = list(map(int,input().split()))
num = Counter(s)
if len(num) <= k:
    print(0)
else:
    n = len(num) - k
    a = 0
    ans = 0
    for i in sorted(num.values()):
        if a == n:
            break
        
        ans += i
        a += 1
        
    print(ans)
