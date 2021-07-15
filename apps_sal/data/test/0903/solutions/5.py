n, k = [int(s) for s in input().split()]
arr = sorted([int(s) for s in input().split()])
arr = arr[::-1]
arr = [pow(10, 11)] + arr[0:(n // 2 + 1)]
n = len(arr)
point = n - 1
while(k != 0):
    t = min(k, (n - point) * (arr[point - 1] - arr[point]))
    k -= t
    arr[point] += t // (n - point)
    if k != 0:
        point -= 1
print(arr[point])
