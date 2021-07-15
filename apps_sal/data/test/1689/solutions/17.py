n = int(input())
config = []
for i in range(n):
    config.append(list(input()))
canSit = False
for i in range(n):
    if canSit:
        continue
    else:
        a, b, c, d, e = config[i]
        if a == 'O' and b == 'O':
            canSit = True
            ans = (i, 1, 2)
        elif d == 'O' and e == 'O':
            canSit = True
            ans = (i, 4, 5)
        else:
            continue
if not canSit:
    print("NO")
else:
    print("YES")
    config[ans[0]][ans[1] - 1] = '+'
    config[ans[0]][ans[2] - 1] = '+'
    for row in config:
        print(''.join(row))

