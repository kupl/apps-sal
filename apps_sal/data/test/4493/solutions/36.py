arr = []
for _ in range(3):
    arr += list(map(int, input().split()))
a = [0] * 3
b = [0] * 3
a[0] = 0
b[0] = arr[0]
b[1] = arr[1]
b[2] = arr[2]
a[1] = arr[4] - b[1]
a[2] = arr[8] - b[2]
tmp = [a[i] + b[j] for i in range(3) for j in range(3)]
print('Yes' if arr == tmp else 'No')
