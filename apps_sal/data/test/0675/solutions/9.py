m, t, r = map(int, input().split())
arr = [int(x) for x in input().split()]
arr.reverse()

ans, tmp = 0, [0 for _ in range(620)]
for i in range(len(arr)):

    candles = 0
    for j in range(arr[i]-1+310, arr[i]-t-1+310, -1):
        if tmp[j] == 1:
            candles += 1
    
    for j in range(arr[i]-t+310, arr[i]+310):
        if candles >= r:
            break
        if tmp[j] == 0:
            tmp[j] = 1
            candles += 1
            ans += 1
            #print(j-310)

    if candles < r:
        ans = -1
        break

print(ans)
