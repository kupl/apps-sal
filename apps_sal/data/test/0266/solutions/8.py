(m, s) = map(int, input().split())
if s > m * 9:
    print(-1, -1)
elif s == 0:
    if m == 1:
        print(0, 0)
    else:
        print(-1, -1)
else:
    pos = 0
    lost = s
    minAns = ''
    while (m - pos - 1) * 9 > lost:
        if pos == 0:
            minAns += '1'
            lost -= 1
        else:
            minAns += '0'
        pos += 1
    if 9 * (m - pos) == lost:
        minAns += '9' * (m - pos)
    else:
        minAns += str(lost % 9) + '9' * (m - pos - 1)
    print(minAns, end=' ')
    maxAns = ''
    lost = s
    pos = 0
    while lost - 9 >= 0:
        maxAns += '9'
        pos += 1
        lost -= 9
    if m - pos > 0:
        maxAns += str(lost)
        maxAns += '0' * (m - pos - 1)
    print(maxAns)
