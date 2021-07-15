l,r = list(map(int,input().split()))

if r-l >=2019 :
    ans = 0 
else :
    ans = 2019**2
    for i in range(l,r+1):
        for j in range(i+1,r+1):
            tmp = i*j%2019
            ans = min(ans,tmp)
print(ans)    

