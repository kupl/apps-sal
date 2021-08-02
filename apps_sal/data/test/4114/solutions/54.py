N = int(input())
l = [list(map(int, input().split())) for i in range(N)]
for i, j, k in l:
    if k > 0:
        fx, fy, fh = i, j, k
for i in range(0, 101):  # x
    for j in range(0, 101):  # y
        sw = 0
        cer_h = fh + abs(fx - i) + abs(fy - j)
        for x, y, h in l:
            if max(cer_h - abs(i - x) - abs(j - y), 0) != h:
                sw = 1
                break
        if sw == 0:
            print(i, j, cer_h)
            return
