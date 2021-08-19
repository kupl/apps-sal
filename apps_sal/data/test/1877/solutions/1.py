N = int(input())
moves = input()

# print(N)
# print(moves)

pos_x, pos_y = 0, 0
coins = 0
kingdom = None
for m in moves:
    if m == "R":
        pos_x += 1
    else:
        pos_y += 1
    if pos_x < pos_y:
        if kingdom == "lower":
            coins += 1
        kingdom = "upper"
    if pos_x > pos_y:
        if kingdom == "upper":
            coins += 1
        kingdom = "lower"

print(coins)
