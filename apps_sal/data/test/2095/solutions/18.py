n = int(input())
row = [[int(x) for x in input().split()] for i in range(n)]
col = [[row[i][j] for i in range(n)] for j in range(n)]
ans = [i for i in range(1, n + 1)]
for i in range(1, n + 1):
    if 1 in row[i - 1] or 3 in row[i - 1] or 2 in col[i - 1] or (3 in col[i - 1]):
        try:
            ans.remove(i)
        except:
            pass
print(len(ans))
print(' '.join([str(x) for x in ans]))
