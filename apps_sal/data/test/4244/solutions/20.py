N = int(input())
X_ls = list(map(int, input().split(' ')))
rst = -1
for i in range(min(X_ls), max(X_ls) + 1):
    val = 0
    for j in X_ls:
        val += (i - j) ** 2
    if rst == -1:
        rst = val
    else:
        rst = min(rst, val)
print(rst)
