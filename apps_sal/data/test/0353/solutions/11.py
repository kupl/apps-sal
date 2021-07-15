n = int(input().strip())
a = list(map(int, input().split()))
if a[-1] == 15:
    print('DOWN')
elif a[-1] == 0:
    print('UP')
else:
    if n == 1:
        print(-1)
    else:
        if a[-2] < a[-1]:
            print('UP')
        else:
            print('DOWN')

