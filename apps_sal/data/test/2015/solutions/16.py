t = int(input())
for _ in range(t):
    lamps = sorted(list(map(int, input().split())))
    if lamps[0] + lamps[1] >= lamps[2] - 1:
        print('Yes')
    else:
        print('No')
