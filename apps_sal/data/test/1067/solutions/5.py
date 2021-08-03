n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
countn = 0
count0 = 0
for i in range(n):
    if(arr[i] < 0):
        countn += 1
        ans += (-1 - arr[i])
    elif(arr[i] > 0):
        ans += arr[i] - 1
    else:
        count0 += 1

if(countn % 2 != 0):
    if(count0 > 0):
        ans += count0
        count0 = 0
    else:
        ans += 2
ans += count0
print(ans)
