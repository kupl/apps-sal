n = int(input().strip())
arr = [int(x) for x in input().strip().split(' ')]
if n == 1:
    if arr[0] == 0:
        print('UP')
    elif arr[0] == 15:
        print('DOWN')
    else:
        print(-1)
else:
    if arr[n - 1] == 0:
        print('UP')
    elif arr[n - 1] == 15:
        print('DOWN')
    else:
        print('UP' if arr[n - 1] > arr[n - 2] else 'DOWN')
