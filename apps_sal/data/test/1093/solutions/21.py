strin1 = str(input())
n = int(strin1.split()[0])
m = int(strin1.split()[1])
arr = [0]*m
for i in range(n):
    currStr = str(input())
    for j in range(m):
        if((currStr[j] == '*') & (arr[j]==0)):
            arr[j] = n-i
maxUp = 0
maxDown = 0
for i in range(m-1):
    if(arr[i+1] > arr[i]):
        maxUp = max(arr[i+1]-arr[i],maxUp) 
    if(( i > 0)&(arr[i]<arr[i-1])):
        maxDown = max(arr[i-1]-arr[i],maxDown)
    if (( i == m-2)&(arr[i]>arr[i+1])):
        maxDown = max(arr[i] - arr[i+1],maxDown)
        
print(maxUp,maxDown)

