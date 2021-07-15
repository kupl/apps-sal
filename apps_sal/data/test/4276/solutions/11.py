
n,T = list(map(int,input().split()))
ans = 1001
for i in range(n):
    c,t = list(map(int,input().split()))
    if t <= T :
        ans = min(ans,c)
        
print((ans if ans!=1001 else "TLE"))  

