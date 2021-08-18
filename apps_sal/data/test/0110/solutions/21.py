INF = 1000_000_000


t = 1

for test in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(max(arr[0], -arr[0] - 1))
    else:
        for i in range(n):
            if arr[i] >= 0:
                arr[i] = -arr[i] - 1
        if n % 2 == 1:
            minval = INF
            ind = -1
            for i in range(n):
                if arr[i] < minval:
                    minval = arr[i]
                    ind = i
            arr[ind] = -arr[ind] - 1
        print(*arr)
