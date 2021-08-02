[n, q] = list(map(int, input().split()))
arr = list(map(int, input().split()))
interval = [idx for idx in range(n)]
l, r = 0, 1
while(l <= r and r < n):
    while(r < n and arr[r] >= arr[r - 1]):
        r += 1
    last = r
    while(r < n and arr[r] <= arr[r - 1]):
        if(arr[r] != arr[last]):
            last = r
        r += 1
    for idx in range(l, r):
        interval[idx] = max(interval[idx], r - 1)
    l = last

ans = []
for _ in range(q):
    [l, r] = list(map(int, input().split()))
    if(interval[l - 1] >= r - 1):
        ans.append('Yes')
    else:
        ans.append('No')
for x in ans:
    print(x)
