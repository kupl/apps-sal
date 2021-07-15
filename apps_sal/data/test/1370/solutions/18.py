from itertools import product
import numpy as np
HWK,*sss = open(0).read().splitlines()
H,W,K = map(int, HWK.split())
sss = [list(map(int, list(ss))) for ss in sss]
sss = np.cumsum(sss, axis=0)
 
if H == 1 or W == 1:
    print(0--sss[-1][-1]//K)
    return
 
ans = float('inf')
for flgs in product([False, True], repeat=H-1):
    cnt = sum(flgs)
    tsss = sss[[*flgs, True]]
    tsss = np.concatenate((tsss[:1], np.diff(tsss, axis=0)), axis=0).T
 
    tmp = 0
    succ = True
    for cur in tsss:
        new = tmp + cur
        if new.max() <= K:
            tmp = new
        else:
            cnt += 1
            if cur.max() > K:
                succ = False
                break
            else:
                tmp = cur
#     print(flgs)
#     print(cnt, ans, tsss)
    if succ:
        ans = min(ans, cnt)
 
print(ans)
