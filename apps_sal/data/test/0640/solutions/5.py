a, b = list(map(int, input().split()))
wins = 0
loss = 0
draw = 0
for i in range(1, 7):
    if abs(a - i) < abs(b - i):
        wins += 1
    elif abs(a - i) > abs(b - i):
        loss += 1
    else:
        draw += 1

print(wins, draw, loss)
