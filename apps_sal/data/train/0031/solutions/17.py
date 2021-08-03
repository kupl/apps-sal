t = int(input())
for _ in range(t):
    crd = set()
    path = input()
    x, y = 0, 0
    sum = 0
    for c in path:
        if c == 'N':
            if (x, y - 1, x, y) in crd:
                sum += 1
            elif (x, y, x, y - 1) in crd:
                sum += 1
            else:
                crd.add((x, y - 1, x, y))
                sum += 5
            x, y = x, y - 1
        elif c == 'S':
            if (x, y + 1, x, y) in crd:
                sum += 1
            elif (x, y, x, y + 1) in crd:
                sum += 1
            else:
                crd.add((x, y + 1, x, y))
                sum += 5
            x, y = x, y + 1
        elif c == 'W':
            if (x + 1, y, x, y) in crd:
                sum += 1
            elif (x, y, x + 1, y) in crd:
                sum += 1
            else:
                crd.add((x + 1, y, x, y))
                sum += 5
            x, y = x + 1, y
        elif c == 'E':
            if (x - 1, y, x, y) in crd:
                sum += 1
            elif (x, y, x - 1, y) in crd:
                sum += 1
            else:
                crd.add((x - 1, y, x, y))
                sum += 5
            x, y = x - 1, y
    print(sum)
