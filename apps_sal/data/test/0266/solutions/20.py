(a, b) = map(int, input().split(' '))
if [a, b] == [1, 0]:
    print('0 0')
elif 1 <= b <= 9 * a:
    haloe = []
    max9 = b // 9
    other = b % 9
    if other != 0:
        strx = '9' * max9 + str(other) + (a - max9 - 1) * '0'
    else:
        strx = '9' * max9 + (a - max9) * '0'
    haloe.append(strx)
    strx = strx[::-1]
    if strx[0] != '0':
        haloe.append(strx)
    else:
        bad = False
        newstr = '1'
        for i in range(1, len(strx)):
            if strx[i] != '0' and (not bad):
                newstr += str(int(strx[i]) - 1)
                bad = not bad
            else:
                newstr += strx[i]
        haloe.append(newstr)
    print(haloe[1] + ' ' + haloe[0])
else:
    print(-1, -1)
