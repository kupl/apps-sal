for _ in range(int(input())):
    n = int(input())
    packs = [(0, 0)]
    for _ in range(n):
        packs.append(tuple(map(int, input().split())))

    packs = sorted(packs)

    res = ''
    for i in range(n):
        dx, dy = packs[i+1][0] - packs[i][0], packs[i+1][1] - packs[i][1]
        if dy < 0:
            res = 'NO'
            break
        
        res += 'R' * dx + 'U' * dy

    #print(packs)
    if res != 'NO':
        print('YES')
        print(res)
    else:
        print(res)

