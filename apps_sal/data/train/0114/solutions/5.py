import sys
for _ in range(int(input())):
    n = int(sys.stdin.readline())
    mons = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    _heros = sorted((tuple(map(int, sys.stdin.readline().split())) for _ in range(m)), reverse=True)
    max_s = 0
    pows = []
    endu = []
    for i in range(m):
        if max_s >= _heros[i][1]:
            continue
        max_s = max(max_s, _heros[i][1])
        pows.append(_heros[i][0])
        endu.append(_heros[i][1])
    pows.append(0)
    endu.append(10 ** 9)
    i = 0
    for ans in range(1, 10 ** 9):
        hero_i = 0
        power = pows[0]
        mons_power = 0
        if power < mons[i]:
            print(-1)
            break
        for j in range(1, n - i + 1):
            if endu[hero_i] < j:
                hero_i += 1
                power = pows[hero_i]
            mons_power = max(mons_power, mons[i])
            if power < mons_power:
                break
            i += 1
        else:
            print(ans)
            break
