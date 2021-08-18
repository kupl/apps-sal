h, w = tuple(map(int, input().split()))

arr = [['r'] * w for i in range(h)]

H = list(map(int, input().split()))
for i, j in enumerate(H):
    arr[i][:j] = ['b'] * j
    if j < w:
        arr[i][j] = 'w'

W = list(map(int, input().split()))
error = False
for i, j in enumerate(W):
    for k in range(j):
        if arr[k][i] == 'w':
            error = True
            break
        else:
            arr[k][i] = 'b'
    if j < h and arr[j][i] == 'b':
        error = True
        break
    elif j < h:
        arr[j][i] = 'w'


if error:
    print(0)
else:
    count = 0
    for i in arr:
        count += i.count('r')
    print((2 ** count) % (10 ** 9 + 7))
