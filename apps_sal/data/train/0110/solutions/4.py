t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    peaks = [0] * (n)
    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            peaks[i] = 1
    acum = [0]
    for i in range(1, n):
        acum.append(acum[-1] + peaks[i])
    maxs = 0
    pos = -1
    for i in range(n - k, -1, -1):
        tmp = acum[i + k - 1] - acum[i]
        if peaks[i + k - 1] == 1:
            tmp -= 1
        if tmp >= maxs:
            maxs = tmp
            pos = i
    print(maxs + 1, pos + 1)
