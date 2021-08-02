n = int(input())
a = [int(_) for _ in input().split()]
if a[-1] == 15:
    print('DOWN')
elif a[-1] == 0:
    print('UP')
elif n == 1:
    print(-1)
elif a[-1] > a[-2]:
    print('UP')
else:
    print('DOWN')
