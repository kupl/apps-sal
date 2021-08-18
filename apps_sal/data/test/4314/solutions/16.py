import copy
h, w = map(int, input().split())
a = [input() for i in range(h)]
index = 1
ans = copy.copy(a)
for i in range(h):
    bool = True
    for j in range(w):
        if a[i][j] == '
        bool = False
    if bool:
        index -= 1
        del ans[index + i]
ans_1 = copy.copy(ans)
key = 1
for i in range(w):
    bool = True
    for j in range(h - (1 - index)):
        if ans[j][i] == '
        bool = False
    if bool:
        key -= 1
        for k in range(h - (1 - index)):
            ans_1[k] = ans_1[k][:(i + key)] + ans_1[k][(i + key + 1):]
for i in range(len(ans_1)):
    print(ans_1[i])
