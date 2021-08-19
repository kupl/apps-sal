import copy

s = input()
t = input()

sn = len(s)
tn = len(t)
a = [[] for i in range(26)]
for i in range(sn):
    num = ord(s[i]) - 97
    a[num].append(i)

table = [[0] * sn for i in range(26)]
for i in range(26):
    if a[i]:
        table[i][:] = [copy.deepcopy(a[i][0])] * sn
    f = 0
    for j in a[i]:
        table[i][f:j] = [copy.deepcopy(j)] * (j - f)
        f = copy.deepcopy(j)

flg = True
cnt = 0  # 今何週したか
x = -1  # 今何文字目か
for i in range(tn):
    num = ord(t[i]) - 97
    # sの中に対象の文字が存在しない
    if not a[num]:
        flg = False
        break
    # sの中に対象の文字が存在
    xx = copy.deepcopy(x)
    x = table[num][x]
    if xx >= x:
        cnt += 1
print(cnt * sn + x + 1) if flg else print(-1)
