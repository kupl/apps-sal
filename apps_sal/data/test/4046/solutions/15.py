from itertools import accumulate
n = int( input())
Q = list( map( int, input().split()))
P = list( accumulate([0] + Q))
m = min(P) - 1
ANS = list( [x-m for x in P])
V = [0]*n
ans = 1
for i in range(n):
    if ANS[i] <= n:
        if V[ANS[i]-1] == 1:
            ans = 0
            break
        V[ANS[i]-1] = 1
    else:
        ans = 0
if ans == 1:
    print(" ".join( map( str, ANS)))
else:
    print(-1)

