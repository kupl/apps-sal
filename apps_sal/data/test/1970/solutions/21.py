t = int(input())
for _ in range(t):
    s = [input() for i in range(8)]
    oh = True
    flag = True
    for i in range(8):
        for j in range(8):
            if(s[i][j] == 'K'):
                if(flag):
                    pos1x = i
                    pos1y = j
                    flag = False
                else:
                    pos2x = i
                    pos2y = j
    if(pos1x % 4 == pos2x % 4) and (pos1y % 4 == pos2y % 4):
        print('YES')
    else:
        print('NO')
    if(_ < t - 1):
        k = input()
