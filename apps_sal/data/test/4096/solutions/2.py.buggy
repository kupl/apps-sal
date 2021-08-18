n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
ans = 0
arr.sort(reverse=True)
flag = 0
for i in range(1, 101):
    days = i
    interval = n // i
    temp = n % i
    tempans = 0
    j = 0
    count = 0
    while(j <= n):
        k = j
        while(k < min(j + i, n)):
            tempans += max(arr[k] - count, 0)
            k += 1
        j += i
        count += 1
    if(tempans >= m):
        print(i)
        flag = 1
        return
if(flag == 0):
    print(-1)
