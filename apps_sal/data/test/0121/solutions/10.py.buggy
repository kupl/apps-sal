def check(A):
    for x1 in range(4):
        for y1 in range(4):
            for x2 in range(4):
                for y2 in range(4):
                    for x3 in range(4):
                        for y3 in range(4):
                            if A[x1][y1] == A[x2][y2] == A[x3][y3] == 'x':
                                # print('!')
                                if x1 == x2 == x3 and y1 == y2 + 1 == y3 + 2:
                                    return True
                                if y1 == y2 == y3 and x1 == x2 + 1 == x3 + 2:
                                    return True
                                if x1 == x2 + 1 == x3 + 2 and y1 == y2 + 1 == y3 + 2:
                                    return True
                                if x1 == x2 + 1 == x3 + 2 and y3 == y2 + 1 == y1 + 2:
                                    return True
    return False


A = [0] * 4
for i in range(4):
    A[i] = list(input())
for i in range(4):
    for j in range(4):
        if A[i][j] == '.':
            A[i][j] = 'x'
            # print(A)
            if check(A):
                print('YES')
                return
            A[i][j] = '.'
print('NO')
