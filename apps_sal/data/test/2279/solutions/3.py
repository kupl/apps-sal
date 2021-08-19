n = int(input())
strs = [list(map(int, input().split())) for _ in range(2 * n - 1)]
entries = sorted(((v, i, j) for (i, row) in enumerate(strs) for (j, v) in enumerate(row)), reverse=True)
ans = [-1] * (2 * n)
for (v, i, j) in entries:
    i += 1
    if ans[i] != -1 or ans[j] != -1:
        continue
    ans[i] = j + 1
    ans[j] = i + 1
print(' '.join(map(str, ans)))
