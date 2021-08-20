(n, x, y) = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
s = 0
for i in range(n):
    if x * 2 >= arr[i]:
        x -= arr[i] // 2
        arr[i] %= 2
    else:
        arr[i] -= x * 2
        x = 0
    if y >= arr[i]:
        y -= arr[i]
        arr[i] = 0
    if x >= arr[i]:
        x -= arr[i]
        arr[i] = 0
    if arr[i] > 0:
        break
    s += 1
print(s)
