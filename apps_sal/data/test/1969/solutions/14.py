n = int(input())
seq = []
for i in range(n):
    seq.append(list(input()))
ans = 0
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if seq[i][j] == 'X' and seq[i - 1][j - 1] == 'X' and (seq[i - 1][j + 1] == 'X') and (seq[i + 1][j - 1] == 'X') and (seq[i + 1][j + 1] == 'X'):
            ans += 1
print(ans)
