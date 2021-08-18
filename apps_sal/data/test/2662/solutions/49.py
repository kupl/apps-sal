

import bisect

n = int(input())

ans = 0
mylist = []
for i in range(n):
    k = int(input())
    idx = bisect.bisect(mylist, -k)
    if idx == ans:
        mylist.append(-k)
        ans += 1
    else:
        mylist[idx] = -k

print(ans)
