n, k = map(int, input().split())

if n == 0:
    print(0)
else:
    arr = [0] * 2 * n
    for i in range(2 * n):
        arr[i] = i + 1

for i in range(0, 2 * k, 2):
    temp = arr[i]
    arr[i] = arr[i + 1]
    arr[i + 1] = temp

for i in range(2 * n):
    print(arr[i], sep=' ', end=' ')

