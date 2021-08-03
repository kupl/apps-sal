N = int(input())
S = input()

rooms = [0] * 10
for c in S:
    if c == 'L':
        i = 0
        while rooms[i]:
            i += 1
        rooms[i] = 1
    elif c == 'R':
        i = 9
        while rooms[i]:
            i -= 1
        rooms[i] = 1
    else:
        rooms[int(c)] = 0

print(''.join(map(str, rooms)))
