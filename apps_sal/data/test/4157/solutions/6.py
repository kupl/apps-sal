n = int(input())
t = [*map(int, input().split())]
x = []
for i in t:
    (twoCnt, threeCnt) = (0, 0)
    tt = i
    while tt % 2 == 0:
        tt //= 2
        twoCnt += 1
    tt = i
    while tt % 3 == 0:
        tt //= 3
        threeCnt += 1
    x.append([i, twoCnt, threeCnt])
x.sort(key=lambda x: (-x[2], x[1]))
for i in x:
    print(i[0], end=' ')
