(n, m) = list(map(int, input().split()))
used = [[True] * m for i in range(n)]
Pole = [0] * n
M = []
for i in range(n):
    Pole[i] = list(input())
for i in range(n):
    for g in range(m):
        if Pole[i][g] == '*':
            k = 0
            while i - k - 1 >= 0 and i + k + 1 < n and (g - k - 1 >= 0) and (g + k + 1 < m):
                if Pole[i - k - 1][g] == '*' and Pole[i + k + 1][g] == '*' and (Pole[i][g - k - 1] == '*') and (Pole[i][g + k + 1] == '*'):
                    used[i - k - 1][g] = False
                    used[i + k + 1][g] = False
                    used[i][g - k - 1] = False
                    used[i][g + k + 1] = False
                    k += 1
                    continue
                break
            if k != 0:
                used[i][g] = False
                M.append([i + 1, g + 1, k])
for i in range(n):
    for g in range(m):
        if Pole[i][g] == '*':
            if used[i][g]:
                print(-1)
                break
    else:
        continue
    break
else:
    print(len(M))
    for i in range(len(M)):
        print(*M[i])
