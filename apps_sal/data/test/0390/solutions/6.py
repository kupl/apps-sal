n, a, b = list(map(int, input().split()))
arr = list(map(int, input().split()))
flag = 0
ans = 0
i = 0
j = n - 1
while(i < j):
    if(arr[i] == 2):
        if(arr[j] == 2):
            ans += 2 * min(a, b)
        else:
            if(arr[j] == 0):
                ans += a
            else:
                ans += b
    else:
        if(arr[j] == 2):
            if(arr[i] == 0):
                ans += a
            else:
                ans += b
        else:
            if(arr[j] != arr[i]):
                flag = 1
                break
    i += 1
    j -= 1
if(n % 2 != 0):
    if(arr[n // 2] == 2):
        ans += min(a, b)
if(flag == 1):
    print(-1)
else:
    print(ans)
