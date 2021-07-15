ans = 0
t = 4*60
n,k = map(int,input().split())
for j in range(n):
    t -= 5*(j+1)
    if t >= k:
        ans +=1
        
    else:
        break
print(ans)
