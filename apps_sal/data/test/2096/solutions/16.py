from sys import stdin

n = int(stdin.readline())
a = [int(x) for x in stdin.readline().split()]
a = sorted([(a[x], x) for x in range(n * 2)])

group = {}

for x, ind in a:
    if x in group:
        group[x].append(ind)
    else:
        group[x] = [ind]

g2 = []

for x in group:
    g2.append([len(group[x]), group[x]])

g2.sort()

left = 0
right = 0

board = [0 for x in range(n * 2)]

ind = 0
for x, l in g2:
    if x == 1:
        ind += 1
        if left <= right:
            left += 1
            board[l[0]] = '1'
        else:
            right += 1
            board[l[0]] = '2'
    else:
        break

if right > left:
    turn = True
else:
    turn = False

for x, l in g2[ind:]:
    left += 1
    right += 1

    if x % 2 == 1:
        last = l.pop()
        if turn:
            board[last] = '1'
        else:
            board[last] = '2'
        turn = not turn
    for n in l[::2]:
        board[n] = '1'
    for n in l[1::2]:
        board[n] = '2'
print(left * right)
print(' '.join(board))
