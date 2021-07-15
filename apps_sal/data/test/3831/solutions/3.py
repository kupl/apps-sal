# https://codeforces.com/contest/883/problem/K
# WA
import heapq
from heapq import heappush as push_
from heapq import heappop  as pop_

n  =  int(input())
p  =  [list(map(int, input().split())) for _ in range(n)] 
Q  =  []
d  =  [s+g for s, g in p]

for i, [s, g] in enumerate(p):
    push_(Q, (s+g, i))
    
flg = True
while len(Q) > 0:
    S, ind = pop_(Q)
    
    if S > d[ind]:
        continue
    
    if ind > 0 and d[ind-1] > S+1:
        if S+1 < p[ind-1][0]:
            flg=False
            break
            
        d[ind-1]  = S+1
        push_(Q, (d[ind-1], ind-1))
        
    if ind < n-1 and d[ind+1] > S+1:
        if S+1 < p[ind+1][0]:
            flg=False
            break
            
        d[ind+1]  = S+1
        push_(Q, (d[ind+1], ind+1))    
    
if flg==False:
    print(-1)
else:
    print(sum([d[i]-p[i][0] for i in range(n)]))
    print(' '.join([str(x) for x in d]))
    
#3
#4 5
#4 5
#4 10       

#4
#1 100
#100 1
#1 100
#100 1

#3
#1 1
#100 100
#1 1

