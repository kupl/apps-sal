N,M = map(int,input().split())
 
#AC,WA
P = [0]*N
Penalty = 0
Accepted = 0
 
for i in range(M) :
    p,S = input().split()
    p = int(p)
    
    if S == "AC" and P[p-1] != -1:
        Penalty += P[p-1]
        Accepted += 1
        P[p-1] = -1
    elif S == "WA" and P[p-1] != -1:
        P[p-1] += 1

print(Accepted,Penalty)
