n = int(input())
m = int(input())
n = n % 6
arr = [0, 0, 0]
arr[m] = 1
for i in range(6 - n):
    j = 6 - n + i
    if j % 2 == 0:
        arr[0], arr[1] = arr[1], arr[0]
    else:
        arr[1], arr[2] = arr[2], arr[1]
print(arr.index(1))
