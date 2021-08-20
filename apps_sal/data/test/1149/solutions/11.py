n = int(input())
littleX = list(map(int, input().split()))
littleY = list(map(int, input().split()))
game = littleX[1:] + littleY[1:]
game = set(game)
if len(game) >= n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
