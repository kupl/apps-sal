def func(i, j, t):
    if i > 0:
        if A[i - 1][j][t] == '1':
            if i < n - 1:
                if A[i + 1][j][t] == '1':
                    return True
            if j < m - 1:
                if A[i][j + 1][t] == '1' and A[i - 1][j + 1][t] == '0':
                    return True
            if t < k - 1:
                if A[i - 1][j][t + 1] == '0' and A[i][j][t + 1] == '1':
                    return True
    if j > 0:
        if A[i][j - 1][t] == '1':
            if j < m - 1:
                if A[i][j + 1][t] == '1':
                    return True
            if i < n - 1:
                if A[i + 1][j][t] == '1' and A[i + 1][j - 1][t] == '0':
                    return True
            if t < k - 1:
                if A[i][j - 1][t + 1] == '0' and A[i][j][t + 1] == '1':
                    return True
    if t > 0:
        if A[i][j][t - 1] == '1':
            if t < k - 1:
                if A[i][j][t + 1] == '1':
                    return True
            if i < n - 1:
                if A[i + 1][j][t] == '1' and A[i + 1][j][t - 1] == '0':
                    return True
            if j < m - 1:
                if A[i][j + 1][t - 1] == '0' and A[i][j + 1][t] == '1':
                    return True

    return False


n, m, k = list(map(int, input().split()))
A = [0] * n
for i in range(n):
    A[i] = [0] * m
    for j in range(m):
        A[i][j] = [0] * k
for i in range(n):
    for j in range(m):
        per = input()
        for t in range(k):
            A[i][j][t] = per[t]
    if i != n - 1:

        per = input()
answer = 0
for i in range(n):
    for j in range(m):
        for t in range(k):
            if A[i][j][t] == '1':
                if func(i, j, t):
                    answer += 1

print(answer)
