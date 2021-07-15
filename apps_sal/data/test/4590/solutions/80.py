n,m,k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

from itertools import accumulate
import bisect
cumsum_a = list(accumulate(a))
cumsum_b = list(accumulate(b))

ans = 0
for i in range(1, n+1):
    if cumsum_a[i-1] > k:
        break
    
    cnt_b = bisect.bisect(cumsum_b, k - cumsum_a[i-1])
    ans = max(ans, i + cnt_b)

for i in range(1, m+1):
    if cumsum_b[i-1] > k:
        break
    
    cnt_a = bisect.bisect(cumsum_a, k - cumsum_b[i-1])
    ans = max(ans, i + cnt_a)

print(ans)
