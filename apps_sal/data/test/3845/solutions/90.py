(a, b) = map(int, input().split())
(cntA, cntB) = (0, 0)
print(100, 100)
flag = False
if a >= b:
    arr = [['#'] * 100 for i in range(100)]
    l = []
    cntB = 1
    for i in range(2, 99, 4):
        if flag:
            break
        for j in range(2, 99, 4):
            l.append((i, j))
            for y in range(i - 1, i + 2):
                for x in range(j - 1, j + 2):
                    arr[y][x] = '.'
            cntA += 1
            if cntA == a:
                flag = True
                break
    while cntB < b:
        cntB += 1
        (s, t) = l.pop()
        arr[s][t] = '#'
    for i in range(100):
        print(''.join(arr[i]))
else:
    arr = [['.'] * 100 for i in range(100)]
    l = []
    cntA = 1
    for i in range(2, 99, 4):
        if flag:
            break
        for j in range(2, 99, 4):
            l.append((i, j))
            for y in range(i - 1, i + 2):
                for x in range(j - 1, j + 2):
                    arr[y][x] = '#'
            cntB += 1
            if cntB == b:
                flag = True
                break
    while cntA < a:
        cntA += 1
        (s, t) = l.pop()
        arr[s][t] = '.'
    for i in range(100):
        print(''.join(arr[i]))
