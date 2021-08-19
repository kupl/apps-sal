n = int(input())
r = l = 0
right_pos = {}
left_pos = {}
for _ in range(n):
    (com, id) = input().split()
    if com == 'R':
        right_pos[id] = r
        r += 1
    elif com == 'L':
        left_pos[id] = l
        l += 1
    elif id in right_pos:
        ind = right_pos[id]
        output = min(l + ind, r - ind - 1)
        print(output)
    else:
        ind = left_pos[id]
        output = min(l - ind - 1, ind + r)
        print(output)
