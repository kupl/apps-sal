n,k= list(map(int,input().split()))
count_0 = 0
count_half = 0
for i in range(1,n+1):
    if i %k == k/2:
        count_half += 1
    elif i%k == 0:
        count_0 += 1
        
print(count_half**3 + count_0**3)
