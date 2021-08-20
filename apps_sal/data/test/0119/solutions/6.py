def solution():
    n = int(input())
    segments = []
    for (i, _) in enumerate(range(n)):
        (x, y) = input().split(' ')
        segments.append((int(x), int(y), i + 1))
    segments = sorted(segments, key=lambda x: (x[0], -x[1]))
    for (i, seg) in enumerate(segments):
        j = i + 1
        if j >= n:
            print('-1 -1')
            return
        while segments[j][1] <= seg[1]:
            print('{} {}'.format(segments[j][2], seg[2]))
            return
    print('-1 -1')
    return


solution()
