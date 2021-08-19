l = [[0] * 5] + [[0] + list(map(int, input().split())) + [0] for _ in range(3)] + [[0] * 5]
ans = [[''] * 3 for _ in range(3)]
for i in range(1, 4):
    for j in range(1, 4):
        ans[i - 1][j - 1] = str(1 - (l[i][j] + l[i][j - 1] + l[i][j + 1] + l[i - 1][j] + l[i + 1][j]) % 2)
print('\n'.join(map(''.join, ans)))
