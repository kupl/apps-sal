import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


h,w,n = list(map(int, input().split()))
from collections import defaultdict, Counter
d = defaultdict(int)
for i in range(n):
    a,b = list(map(int, input().split()))
    for i in range(a-2, a+1):
        for j in range(b-2, b+1):
            if 1<=i<=h-2 and 1<=j<=w-2:
                d[i,j] += 1
ans = [None]*10
ans[0] = (h-2)*(w-2) - len(d)
c = Counter(list(d.values()))
for i in range(1,10):
    if i in c:
        ans[i] = c[i]
    else:
        ans[i] = 0
write("\n".join(map(str, ans)))

