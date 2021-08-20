matrix = []
N = 10
for i in range(N):
    matrix.append(list(input()))
won = False


def check_alice_won(matrix):
    maxScore = 0
    for i in range(N):
        curScore = 0
        for j in range(N):
            if matrix[i][j] == 'X':
                curScore += 1
            else:
                if curScore > maxScore:
                    maxScore = curScore
                curScore = 0
        if curScore >= maxScore:
            maxScore = curScore
        if maxScore >= 5:
            return True
    maxScore = 0
    for i in range(N):
        curScore = 0
        for j in range(N):
            if matrix[j][i] == 'X':
                curScore += 1
            else:
                if curScore > maxScore:
                    maxScore = curScore
                curScore = 0
        if curScore >= maxScore:
            maxScore = curScore
        if maxScore >= 5:
            return True
    maxScore = 0
    for p in range(0, 2 * N - 1):
        curScore = 0
        for q in list(range(max(0, p - N + 1), min(p, N - 1) + 1)):
            if matrix[p - q][q] == 'X':
                curScore += 1
            else:
                if curScore > maxScore:
                    maxScore = curScore
                curScore = 0
        if curScore >= maxScore:
            maxScore = curScore
        if maxScore >= 5:
            return True
    maxScore = 0
    for p in range(0, 2 * N - 1):
        curScore = 0
        for q in list(range(max(0, p - N + 1), min(p, N - 1) + 1)):
            if matrix[p - q][N - 1 - q] == 'X':
                curScore += 1
            else:
                if curScore >= maxScore:
                    maxScore = curScore
                curScore = 0
        if curScore >= maxScore:
            maxScore = curScore
        if maxScore >= 5:
            return True
    return False


for i in range(N):
    for j in range(N):
        if matrix[i][j] == '.' and won == False:
            matrix[i][j] = 'X'
            if check_alice_won(matrix) == True:
                won = True
            matrix[i][j] = '.'
if won:
    print('YES')
else:
    print('NO')
