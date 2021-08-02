matrix = [None] * 10
for i in range(10):
    matrix[i] = input()

for i in range(10):
    for j in range(10):
        if 0 <= j and j <= 5:
            count_x = 0
            has_o = False
            for k in range(5):
                if matrix[i][j + k] == 'X':
                    count_x += 1
                elif matrix[i][j + k] == 'O':
                    has_o = True
                    break
            if count_x == 4 and not has_o:
                print("YES")
                return

            if 0 <= i and i <= 5:
                count_x = 0
                has_o = False
                for k in range(5):
                    if matrix[i + k][j + k] == 'X':
                        count_x += 1
                    elif matrix[i + k][j + k] == 'O':
                        has_o = True
                        break
                if count_x == 4 and not has_o:
                    print("YES")
                    return

        if 0 <= i and i <= 5:
            count_x = 0
            has_o = False
            for k in range(5):
                if matrix[i + k][j] == 'X':
                    count_x += 1
                elif matrix[i + k][j] == 'O':
                    has_o = True
                    break
            if count_x == 4 and not has_o:
                print("YES")
                return

            if 4 <= j and j <= 9:
                count_x = 0
                has_o = False
                for k in range(5):
                    if matrix[i + k][j - k] == 'X':
                        count_x += 1
                    elif matrix[i + k][j - k] == 'O':
                        has_o = True
                        break
                if count_x == 4 and not has_o:
                    print("YES")
                    return
print("NO")
