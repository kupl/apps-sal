n = int(input())
s = ' ' + input()
F = [[-1 for i in range(4)] for j in range(n + 1)]
F[0] = [1, 0, 0, 0]
div = 10 ** 9 + 7
for i in range(1, n + 1):
    if s[i] == '?':
        F[i][0] = 3 * F[i - 1][0] % div
    else:
        F[i][0] = F[i - 1][0] % div
    if s[i] == 'a':
        F[i][1] = (F[i - 1][1] + F[i - 1][0]) % div
    elif s[i] == '?':
        F[i][1] = (3 * F[i - 1][1] + F[i - 1][0]) % div
    else:
        F[i][1] = F[i - 1][1] % div
    if s[i] == 'b':
        F[i][2] = (F[i - 1][2] + F[i - 1][1]) % div
    elif s[i] == '?':
        F[i][2] = (3 * F[i - 1][2] + F[i - 1][1]) % div
    else:
        F[i][2] = F[i - 1][2] % div
    if s[i] == 'c':
        F[i][3] = (F[i - 1][3] + F[i - 1][2]) % div
    elif s[i] == '?':
        F[i][3] = (3 * F[i - 1][3] + F[i - 1][2]) % div
    else:
        F[i][3] = F[i - 1][3] % div
print(F[-1][3])
