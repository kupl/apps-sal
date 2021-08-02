l, times = map(int, input().split(" "))
line = list(map(int, input().split(" ")))
line.sort()
subtracted = 0
curri = 0
for _ in range(times):
    while curri < l and line[curri] <= subtracted: curri += 1
    if curri == l: print(0)
    else:
        v = line[curri]
        print(v - subtracted)
        subtracted = v
