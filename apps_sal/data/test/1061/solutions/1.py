l = [list(map(int, input().split())) for i in range(5)]
for i in range(5):
    line = l[i]
    if 1 in line:
        print(abs(2 - i) + abs(2 - line.index(1)))
