line = input()
if len(line) % 2:
    print(-1)
else:
    x = abs(line.count('U')-line.count('D'))
    y = abs(line.count('R')-line.count('L'))
    print((x + y) // 2)
