n = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
prev = -1
d = dict()
for i in range(n):
    d[brr[i]] = i
ans = 0
for i in range(n):
    if(d[arr[i]] - prev > 0):
        ans += (d[arr[i]] - prev - 1)
        prev = d[arr[i]]

print(ans)
