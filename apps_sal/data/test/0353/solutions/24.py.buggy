n = int(input())
a = list(map(int, input().split()))

if n <= 1:
    if n and a[0] in (0, 15):
        print('UP' if a[0] == 0 else 'DOWN')
        return
    print('-1')
    return

if a[-1] - a[-2] >= 1:
    if a[-1] < 15:
        print('UP')
    else:
        print('DOWN')
else:
    if a[-1] <= 0:
        print('UP')
    else:
        print('DOWN')
