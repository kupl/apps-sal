n = int(input())


b = [[0 for i in range(n + 2)] for j in range(n + 2)]

for i in range(1, n + 1):
    s = input()
    for j in range(1, n + 1):
        if s[j - 1] == 'o':
            b[i - 1][j] += 1
            b[i + 1][j] += 1
            b[i][j + 1] += 1
            b[i][j - 1] += 1
yes = True
for i in range(1, n + 1):
    if not yes:
        break
    for j in range(1, n + 1):
        if b[i][j] % 2 == 1:
            print("NO")
            yes = False
            break
if yes:
    print("YES")
