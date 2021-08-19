import itertools as it


def special(a):
    return a == '#' or a == '*' or a == '&'


(n, m) = list(map(int, input().split()))
INF = 10 ** 6
A = []
for _ in range(n):
    A += [input()]
B = []
for _ in range(3):
    B += [[INF] * n]
for i in range(n):
    if A[i][0].isalpha():
        B[0][i] = 0
    else:
        j = 1
        k = m - 1
        while j <= k:
            if A[i][j].isalpha() or A[i][k].isalpha():
                B[0][i] = j
                break
            j += 1
            k -= 1
for i in range(n):
    if A[i][0].isdigit():
        B[1][i] = 0
    else:
        j = 1
        k = m - 1
        while j <= k:
            if A[i][j].isdigit() or A[i][k].isdigit():
                B[1][i] = j
                break
            j += 1
            k -= 1
for i in range(n):
    if special(A[i][0]):
        B[2][i] = 0
    else:
        j = 1
        k = m - 1
        while j <= k:
            if special(A[i][j]) or special(A[i][k]):
                B[2][i] = j
                break
            j += 1
            k -= 1
result = INF
for pick in it.combinations(list(range(n)), 3):
    for perm in it.permutations(list(range(3))):
        result = min([result, B[perm[0]][pick[0]] + B[perm[1]][pick[1]] + B[perm[2]][pick[2]]])
print(result)
