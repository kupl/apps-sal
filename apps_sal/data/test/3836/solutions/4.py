from math import *
n = int(input())
arr = []
count1 = 0
count2 = 0
ans = 0
for i in range(n):
    a, b = map(str, input().split())
    b = int(b)
    arr.append((b, a))
    if(arr[i][1] == '10'):
        count1 += 1
    elif(arr[i][1] == '01'):
        count2 += 1
    elif(arr[i][1] == '11'):
        count1 += 1
        count2 += 1
    ans += arr[i][0]
arr.sort(reverse=True)
i = n - 1
flag = 0
size = n
minval = min(count1, count2)
while(i >= 0 and (count1 < ceil(size / 2) or count2 < ceil(size / 2))):
    if(arr[i][1] == '00'):
        ans -= arr[i][0]
        size -= 1
    elif(arr[i][1] == '10'):
        if(count1 > minval):
            ans -= arr[i][0]
            count1 -= 1
            size -= 1
    elif(arr[i][1] == '01'):
        if(count2 > minval):
            ans -= arr[i][0]
            count2 -= 1
            size -= 1
    i -= 1
if(i == 0 and (count1 < ceil(size / 2) or count2 < ceil(size / 2))):
    print(0)
else:
    print(ans)
