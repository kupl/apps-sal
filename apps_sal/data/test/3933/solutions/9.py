n = int(input())
u = 0
arr = list(map(int,input().split()))
d = arr[1] - arr[0]
for i in range(n-1):
    if arr[i] + d != arr[i+1]:
        print(arr[n-1])
        u+=1
        break
if u == 0: 
    print(arr[n-1]+d)

