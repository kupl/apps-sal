def variant(cur):
    nonlocal minv
    if len(cur) < len(rooms):
        variant(cur + [0])
        variant(cur + [1])
    else:
        curpos = 0
        time = 0
        for i in range(len(rooms) - 1):
            if curpos != cur[i]:
                time += m + 1
                curpos = cur[i]
            else:
                time += 2 * rooms[i][curpos]
            if i != 0:
                time += 1
        time += rooms[-1][curpos] + 1
        if len(rooms) == 1:
            time -= 1
        minv = min(minv, time)



n, m = map(int, input().split())
minv = 1000000000
rooms = []
stopdel = False

for i in range(n):
    line = input()
    a = 0
    for j in range(m + 2):
        if line[j] == '1':
            a = m + 1 - j
            break
    b = 0
    for j in range(m + 1, -1, -1):
        if line[j] == '1':
            b = j
            break
    if a != 0 or b != 0 or stopdel:
        rooms.append((b, a))
        stopdel = True

rooms = rooms[::-1]

if not rooms:
    print('0')
else:
    variant([])
    print(minv)
