n = int(input())
a = list(map(int, input().split()))
if n > 1:
    if a[n - 1] > a[n - 2]:
        if a[n - 1] == 15:
            print('DOWN')
        else:
            print('UP')
    else:
        if a[n - 1] == 15:
            print('DOWN')
        else:
            if a[n - 1] == 0:
                print('UP')
            else:
                print('DOWN')
else:
    if a[0] == 15:
        print('DOWN')
    else:
        if a[0] == 0:
            print('UP')
        else:
            print(-1)
