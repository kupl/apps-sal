r, c, n = map(int, input().split())
field = []
field.append('
for _ in range(r):
    field.append('
field.append('


p_x=0
p_y=0


not_walls=0
for x in range(1, r + 1):
    for y in range(1, c + 1):
        if field[x][y] == '
            continue
        p_x, p_y=x, y
        not_walls += 1
process=[(p_x, p_y)]
valid=set()

while len(valid) < (not_walls - n):
    x, y=process.pop()
    valid.add((x, y))

    for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if field[a + x][b + y] == '.' and (a + x, b + y) not in valid:
            process.append((x + a, y + b))


for x in range(1, r + 1):
    for y in range(1, c + 1):
        if field[x][y] == '
            continue
        if (x, y) not in valid:
            field[x]=field[x][:y] + 'X' + field[x][y + 1:]

field=[x[1:-1] for x in field[1:-1]]
print('\n'.join(field))
