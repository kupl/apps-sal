pos = input()
moves = 8
if pos[0] in ['a', 'h']:
    moves -= 3
if pos[1] in ['1', '8']:
    moves -= 3
if moves < 3:
    moves = 3
print(moves)
