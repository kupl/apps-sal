n, m = input().split()
n = int(n)
m = int(m)
#print(str(n)+' '+str(m))
arr = []
for i in range(m):
    d, h = input().split()
    arr.append([int(d), int(h)])

last = arr[0]
res = arr[0][1]
for i in range(1, m):
    if arr[i][0] - last[0] < abs(arr[i][1] - last[1]):
        print("IMPOSSIBLE")
        return
    else:
        diff = arr[i][1] - last[1]
        res = max(res, (arr[i][0]-last[0]+diff)//2 + last[1])
        res = max(res, arr[i][1])
        last = arr[i]
print(max(arr[0][1]+arr[0][0]-1, max(res, n - arr[len(arr)-1][0] + arr[len(arr)-1][1]))) 
