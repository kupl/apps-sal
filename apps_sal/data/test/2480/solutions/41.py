import numpy as np
from collections import defaultdict,deque
N,K= list(map(int,input().split()))
A = np.array([1]+list(map(int,input().split())))-1

Acs = np.cumsum(A)
Acs %= K

ans = 0
cnt = defaultdict(deque)
for i,c in enumerate(Acs):
    cnt[c].append(i)
    while cnt[c]:
        if i-cnt[c][0]> K-1:
            cnt[c].popleft()
        else:
            break
    ans += len(cnt[c]) - 1
print(ans)



