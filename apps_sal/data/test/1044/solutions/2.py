n = int(input())
ai = list(map(int, input().split()))
win = 2
for i in ai:
    if i % 2 == 0:
        win = 3 - win
    print(win)
