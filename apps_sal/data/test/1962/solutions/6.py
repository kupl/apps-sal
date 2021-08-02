n, k, l = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr = sorted(arr)
if arr[n - 1] - arr[0] > l:
    print(0)
else:
    maxVol = arr[0] + l
    index = 0
    while index < n * k - 1 and arr[index + 1] <= maxVol:  # index will be at most n * k - 1
        index += 1
    s = arr[0]
    i = 0
    remaining = n - 1
    while remaining > 0 and i + k + remaining - 1 <= index:  # jumps of k
        i += k
        remaining -= 1
        s += arr[i]
    if remaining > 0 and index - (remaining - 1) > 1 + i:  # can now only make a jump of at most k - 1
        i = (index - (remaining - 1))
        s += arr[i]
        remaining -= 1
    while remaining > 0:
        i += 1
        s += arr[i]
        remaining -= 1
    print(s)
