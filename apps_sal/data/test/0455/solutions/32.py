N = int(input())
Points = [list(map(int, input().split())) for i in range(N)]

odd_or_even = set([(x + y) % 2 for x, y in Points])
if len(odd_or_even) == 2:
    print((-1))
    return


D = [2 ** i for i in range(39)]
D = D[::-1]
if 0 in odd_or_even:
    D.append(1)

print((len(D)))
print((' '.join(map(str, D))))
operation = {'R': (-1, 0), 'L': (1, 0), 'U': (0, -1), 'D': (0, 1)}  # 反対にすることに注意
for x, y in Points:
    nx, ny = x, y
    ans = ''
    for d in D:
        best_score = float('inf')
        best_command = None
        next_x, next_y = None, None

        for command, move in list(operation.items()):
            mx, my = move
            tx, ty = nx + d * mx, ny + d * my
            score = abs(tx) + abs(ty)
            if score < best_score:
                best_score = score
                best_command = command
                next_x, next_y = tx, ty

        ans += best_command
        nx, ny = next_x, next_y

    print(ans)

