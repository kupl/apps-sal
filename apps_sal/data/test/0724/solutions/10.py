n, d = list(map(int, input().split()))
arr = [int(x) for x in input().split()]
arr.sort()
start = 0
end = 0
mx = 0
while end < n:
    while end < n and arr[end] - arr[start] <= d:
        end += 1
    mx = max(mx, end - start)
    start += 1
    
mx = max(mx, n - start)

print(n - mx)

