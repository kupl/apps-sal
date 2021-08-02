n = int(input())
a = list(map(int, input().split()))
x = sum(a)
arr = [[-1, 0, 0]]
for i in range(n):

    if i % 2 == 0:
        arr.append([arr[-1][0] + 1, arr[-1][1], '/'])
        for k in range(a[i] - 1):
            arr.append([arr[-1][0] + 1, arr[-1][1] + 1, '/'])
    else:
        arr.append([arr[-1][0] + 1, arr[-1][1], '\\'])
        for k in range(a[i] - 1):
            arr.append([arr[-1][0] + 1, arr[-1][1] - 1, '\\'])
for i in range(len(arr)):
    arr[i][0], arr[i][1] = arr[i][1], -arr[i][0]
arr.pop(0)
arr.sort()
arr = arr[::-1]
for i in range(len(arr)):
    arr[i][1] = - arr[i][1]
print(' ' * arr[0][1], end='')
print(arr[0][2], end='')
for i in range(1, len(arr)):
    if arr[i][0] == arr[i - 1][0]:
        print(' ' * (arr[i][1] - arr[i - 1][1] - 1), end='')
        print(arr[i][2], end='')
    else:
        print(' ' * (x - arr[i - 1][1] - 1))
        print(' ' * arr[i][1], end='')
        print(arr[i][2], end='')
print(' ' * (x - arr[-1][1] - 1), end='')
