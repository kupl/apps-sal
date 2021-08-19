x = [6, 10, 14]
T = int(input())
for _ in range(T):
    y = int(input())
    if y >= sum(x) + 1:
        if y - sum(x) in x:
            print('YES')
            print(6, 10, 15, y - sum(x) - 1)
            continue
        else:
            print('YES')
            print(' '.join(map(str, x)), y - sum(x))
            continue
    print('NO')
