T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    prefix = []
    prefix.append(arr[0])
    mx = arr[0]
    for i in range(1, n):
        mx = max(mx, arr[i])
        prefix.append(arr[i])
        prefix[i] += prefix[i - 1]

    m = {}
    for i in range(0, n):
        for j in range(i + 1, n):
            if i == 0:
                s = prefix[j]
                if s <= mx:
                    m[s] = 0
            else:
                s = prefix[j] - prefix[i - 1]
                if s <= mx:
                    m[s] = 0
    
    ans = 0
    for i in arr:
        if i in m:
            ans += 1

    print(ans)    
