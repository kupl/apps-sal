def calc(c1, c2):
    x = abs(ord(c1) - ord(c2))
    return min(x, 26 - x)


a, b = list(map(int, input().split(' ')))
strx = input()

if a % 2 == 0:
    if b > a // 2:
        b = a + 1 - b
    left = strx[:a // 2]
    right = strx[a // 2:]
    right = right[::-1]
    dist = [calc(left[i], right[i]) for i in range(a // 2)]
    indx = b - 1
    rightpt = b - 1
    leftpt = b - 1
    for i in range(a // 2):
        if dist[i] != 0:
            leftpt = i
            break
    dist.reverse()
    for i in range(a // 2):
        if dist[i] != 0:
            rightpt = (a // 2 - 1) - i
            break

    sumlr = rightpt - leftpt + min(abs(leftpt - indx), abs(rightpt - indx))
    print(sum(dist) + sumlr)

else:
    if b > a // 2 + 1:
        b = a + 1 - b
    left = strx[:a // 2]
    right = strx[a // 2:][1:]
    right = right[::-1]
    dist = [calc(left[i], right[i]) for i in range(a // 2)]
    indx = b - 1
    rightpt = b - 1
    leftpt = b - 1
    for i in range(a // 2):
        if dist[i] != 0:
            leftpt = i
            break
    dist.reverse()
    for i in range(a // 2):
        if dist[i] != 0:
            rightpt = (a // 2 - 1) - i
            break
    sumlr = rightpt - leftpt + min(abs(leftpt - indx), abs(rightpt - indx))
    print(sum(dist) + sumlr)
