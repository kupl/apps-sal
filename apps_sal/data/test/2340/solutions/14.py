q = int(input())
for _ in range(q):
    h, n = list(map(int, input().split()))
    ps = list(map(int, input().split())) + [0, 0]
    ps.reverse()
    cur = n-1
    crystals = 0
    while ps and ps[-1] > 1:
        if ps[-2] == h - 1:
            if ps[-3] == h - 2:
                ps.pop()
                ps.pop()
            else:
                ps.pop()
                ps[-1] = h - 2
                crystals += 1
            h -= 2
        else:
            ps[-1] = ps[-2] + 1
            h = ps[-1]
    print(crystals)

