
dest = list(map(int, input().split()))

side_len = 0
pos = [0, 0]
turns = 0

while True:
    side_len += 1
    if dest[1] == pos[1] and pos[0] <= dest[0] <= pos[0] + side_len:
        break
    turns += 1
    pos[0] += side_len
    if dest[0] == pos[0] and pos[1] <= dest[1] <= pos[1] + side_len:
        break
    turns += 1
    pos[1] += side_len
    side_len += 1
    if dest[1] == pos[1] and pos[0] >= dest[0] >= pos[0] - side_len:
        break
    turns += 1
    pos[0] -= side_len
    if dest[0] == pos[0] and pos[1] >= dest[1] >= pos[1] - side_len:
        break
    turns += 1
    pos[1] -= side_len

print(turns)




