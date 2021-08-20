(x, y, x0, y0) = [int(x) for x in input().split()]
s = input()
was_in = [[False for y1 in range(y + 1)] for x1 in range(x + 1)]
length = 1
moves = {'D': (1, 0), 'U': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
state = (x0, y0)
count = [1]
was_in[x0][y0] = True
for c in s:
    new_state = (state[0] + moves[c][0], state[1] + moves[c][1])
    new_state = new_state if 0 < new_state[0] <= x and 0 < new_state[1] <= y else state
    state = new_state
    if was_in[state[0]][state[1]]:
        count.append(0)
    else:
        count.append(1)
        was_in[state[0]][state[1]] = True
        length += 1
count[-1] += x * y - length
for i in count:
    print(i, end=' ')
