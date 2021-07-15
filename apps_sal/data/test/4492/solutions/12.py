n, x = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = sum(arr)
arr[0] = min(x, arr[0])


for i in range(n-1):
    diff = arr[i] + arr[i+1]
    if diff > x:
        arr[i+1] -= diff - x

print(sum_arr - sum(arr))
