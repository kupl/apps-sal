(n, c) = list(map(int, input().split()))
arr = [int(i) for i in input().split()]
(i, r) = (0, 0)
for i in range(n - 1):
    if arr[i] - arr[i + 1] - c > r:
        r = arr[i] - arr[i + 1] - c
print(r)
