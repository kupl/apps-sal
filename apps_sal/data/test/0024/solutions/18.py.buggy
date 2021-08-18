l = [input() for _ in range(10)]

for c in range(5):
    t = ['X'] * 5
    t[c] = '.'
    for i in range(10):
        for j in range(6):
            cnt = 0
            for k in range(5):
                if l[i][j + k] == '.':
                    cnt += 1
                elif l[i][j + k] == 'O':
                    cnt += 2
            if cnt == 1:
                print('YES')
                return

    for i in range(6):
        for j in range(10):
            cnt = 0
            for k in range(5):
                if l[i + k][j] == '.':
                    cnt += 1
                elif l[i + k][j] == 'O':
                    cnt += 2
            if cnt == 1:
                print('YES')
                return

    for i in range(6):
        for j in range(6):
            cnt = 0
            for k in range(5):
                if l[i + k][j + k] == '.':
                    cnt += 1
                elif l[i + k][j + k] == 'O':
                    cnt += 2
            if cnt == 1:
                print('YES')
                return

    for i in range(4, 10):
        for j in range(6):
            cnt = 0
            for k in range(5):
                if l[i - k][j + k] == '.':
                    cnt += 1
                elif l[i - k][j + k] == 'O':
                    cnt += 2
            if cnt == 1:
                print('YES')
                return

print('NO')
