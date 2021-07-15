from collections import defaultdict as dd, deque

n,k1,k2 = list(map(int,input().split()))
k = k1+k2

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

D = dd(int)

for i in range(n):
    D[abs(A[i]-B[i])] += 1

x = sorted([[k,v] for k,v in list(D.items())], reverse=True)

ops = 0
i = 0
while x[i][0]>0:
    if i<len(x)-1:
        if x[i][0]==x[i+1][0]:
            x[i+1][1] += x[i][1]
            x[i][1] = 0 # oops
            i += 1
    diff,cnt = x[i]
    if k - ops >= cnt:
        x[i][0] -= 1
        ops += cnt
    else:
        x.append((diff-1,k-ops))
        x[i][1] -= k-ops
        ops += k-ops
        break

if ops!=k:
    print(1 if (k-ops)%2 else 0)
else:
    ans = 0
    for diff,cnt in x:
        ans += cnt*(diff)**2
    print(ans)

