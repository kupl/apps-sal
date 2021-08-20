n = int(input())
a = list(map(int, input().split()))
if n == 1 and a[0] != 0 and (a[0] != 15):
    print(-1)
elif a[-1] == 0:
    print('UP')
elif a[-1] == 15:
    print('DOWN')
elif a[-2] < a[-1]:
    print('UP')
elif a[-2] > a[-1]:
    print('DOWN')
