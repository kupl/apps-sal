n = int(input())

gamers = {1: True, 2: True, 3: False}

for i in range(n):
    a = int(input())

    if not gamers[a]:
        print('NO')
        return

    else:
        for j in list(gamers.keys()):
            if j != a:
                gamers[j] = not gamers[j]

print('YES')
