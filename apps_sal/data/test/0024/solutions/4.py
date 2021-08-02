def main():

    Map = []
    for i in range(10):
        Map += [input()]

    for i in range(10):
        for j in range(10):
            count = 0
            count2 = 0
            if i <= 5:
                for k in range(5):
                    if Map[i + k][j] == 'X':
                        count += 1
                    elif Map[i + k][j] == '.':
                        count2 += 1
                if count == 4 and count2 == 1:
                    print('YES')
                    return 0

            count = 0
            count2 = 0
            if j <= 5:
                for k in range(5):
                    if Map[i][j + k] == 'X':
                        count += 1
                    elif Map[i][j + k] == '.':
                        count2 += 1
                if count == 4 and count2 == 1:
                    print('YES')
                    return 0

            count = 0
            count2 = 0

            if i <= 5 and j <= 5:
                for k in range(5):
                    if Map[i + k][j + k] == 'X':
                        count += 1
                    elif Map[i + k][j + k] == '.':
                        count2 = 1
                if count == 4 and count2 == 1:
                    print('YES')
                    return 0
            count = 0
            count2 = 0

            if i >= 4 and j <= 5:
                count = 0
                for k in range(5):
                    if Map[i - k][j + k] == 'X':
                        count += 1
                    elif Map[i - k][j + k] == 'O':
                        count -= 1

                if count == 4:
                    print('YES')
                    return 0
    print('NO')
    return 0


main()
