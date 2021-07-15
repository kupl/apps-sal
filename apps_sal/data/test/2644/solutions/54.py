import copy
N = int(input())
Po = list(map(int,input().split()))
P = copy.deepcopy(Po)
pos = [0 for i in range(N+1)]
for i in range(N) :
    pos[P[i]] = i+1

i = 1
ans = []
while(i < N) :
    j = pos[i]
    if j<=i : break
    for k in range(j-1,i-1,-1) :
        ans.append(k)
        P[k-1],P[k] = P[k],P[k-1]
    i = j
if(len(ans)==N-1 and P == [i+1 for i in range(N)]) :
    for out in ans :
        print(out)
else :
    print(-1)
