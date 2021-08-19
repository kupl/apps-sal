n = int(input())
k = list(map(int, input().split()))
UP = 'UP'
DOWN = 'DOWN'
if k[-1] == 15:
    print(DOWN)
elif k[-1] == 0:
    print(UP)
elif n == 1:
    print(-1)
elif k[-2] > k[-1]:
    print(DOWN)
else:
    print(UP)
