(x, y, xc, yc) = map(int, input().strip().split())
yc -= 1
xc -= 1
program = input().strip()
commands = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
used = [[False] * y for i in range(x)]
used[xc][yc] = True
result = []
print(1, end=' ')
cnt = 1
for i in range(len(program)):
    cmd = program[i]
    xc += commands[cmd][0] if -1 < xc + commands[cmd][0] < x else 0
    yc += commands[cmd][1] if -1 < yc + commands[cmd][1] < y else 0
    if not used[xc][yc] and i != len(program) - 1:
        print(1, end=' ')
        result.append(1)
        cnt += 1
    elif i != len(program) - 1:
        print(0, end=' ')
        result.append(0)
    else:
        print(x * y - cnt, end=' ')
    used[xc][yc] = True
