n,x = list(map(int,input().split()))
narr = list(map(int,input().split()))
c=0
for i in range(1,n):
    total = narr[i]+narr[i-1]
    if(total <= x):
        continue
    else:
        c += (total - x)
        narr[i] = max(0,narr[i]-(total-x))
print(c)

