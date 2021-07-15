n, k = map(int, input().split())
A = [['-'] + list(input()) + ['-'] for _ in range(n)]
neighs = 0
for i in A:
    for j in range(len(i)):
        if i[j] == 'S':
            if i[j - 1] != '.' and i[j - 1] != '-':
                neighs += 1
            if i[j + 1] != '.' and i[j + 1] != '-':
                neighs += 1
for i in range(len(A)):
    if k < 0:
        break
    for j in range(len(A[i])):
        if A[i][j] == '.' and A[i][j - 1] != 'S' and A[i][j + 1] != 'S' and k > 0:
            A[i][j] = 'x'
            k -= 1
        elif k <= 0:
            break
for i in range(len(A)):
    if k < 0:
        break
    for j in range(len(A[i])):
        if A[i][j] == '.' and A[i][j - 1] == 'S' and A[i][j + 1] != 'S' and k > 0:
            A[i][j] = 'x'
            neighs += 1
            k -= 1
        elif k <= 0:
            break
for i in range(len(A)):
    if k < 0:
        break
    for j in range(len(A[i])):
        if A[i][j] == '.' and A[i][j - 1] != 'S' and A[i][j + 1] == 'S' and k > 0:
            A[i][j] = 'x'
            neighs += 1
            k -= 1
        elif k <= 0:
            break
for i in range(len(A)):
    if k < 0:
        break
    for j in range(len(A[i])):
        if A[i][j] == '.' and k > 0:
            A[i][j] = 'x'
            neighs += 2
            k -= 1
        elif k <= 0:
            break
print(neighs)
for i in A:
    print(*i[1:-1], sep='')
