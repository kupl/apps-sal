for _ in range(int(input())):
    n = int(input())
    s = list(input())
    d1 = {}
    d1[(0, 0)] = [0]
    x, y = 0, 0
    i = 1
    for c in s:
        if c == "L":
            x -= 1
        if c == "R":
            x += 1
        if c == "U":
            y += 1
        if c == "D":
            y -= 1
        if (x, y) in d1:
            d1[(x, y)].append(i)
        else:
            d1[(x, y)] = [i]
        i += 1
    answer = -1
    answer_coord = [0, 0]
    for x in d1:
        if len(d1[x]) > 1:
            d1[x].sort()
            for i in range(len(d1[x]) - 1):
                if answer == -1:
                    answer = d1[x][i + 1] - d1[x][i]
                    answer_coord = [d1[x][i + 1], d1[x][i]]
                elif d1[x][i + 1] - d1[x][i] < answer:
                    answer = d1[x][i + 1] - d1[x][i]
                    answer_coord = [d1[x][i + 1], d1[x][i]]
    a = answer_coord[1]
    b = answer_coord[0]
    if answer != -1:
        print(a + 1, b)
    else:
        print(-1)
