import math
n,d = list(map(int,input().split()))
li =[list(map(int,input().split())) for i in range(n)]
cnt = 0
sum = 0

for i in range(n-1):
    for j in range(i+1,n):
        sum = 0
        for x in range(d):
            sum += abs(li[i][x]-li[j][x])**2
        
        if math.sqrt(sum) % 1 == 0.0:
            cnt += 1

print(cnt)

