n = int(input())

data = []
for i in range(n):
    a, b =  list(map(int, input().split()))
    data.append([a,b,0])
    
if (n==1):
    count = 1
else:
    count = 2

for i in range(1,n-1):
    if (data[i][0]-data[i-1][0]>data[i][1]):
        count += 1
    elif (data[i+1][0]-data[i][0]>data[i][1]):
        count += 1
        data[i][0] += data[i][1]

print(count)

