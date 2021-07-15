n,s = [int(i) for i in input().split()]
lst = [0 for i in range(n)]
for i in range(n-1):    
    x,y = [int(i) for i in input().split()]
    lst[x-1]+=1
    lst[y-1]+=1
count = 0
for i in lst:
    if i == 1:
        count+=1

print(2*s/count)

