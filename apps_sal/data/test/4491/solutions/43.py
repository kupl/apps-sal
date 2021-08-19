n = int(input())
a = [list(map(int, input().split())), list(map(int, input().split()))]
ame = 0
ame_l = []
for i in range(n):  # 重複する列の選択
    for j in range(n):  # 各列足してく
        if i > j:
            ame += a[0][j]
        elif i == j:
            ame += a[0][j] + a[1][j]
        else:
            ame += a[1][j]
        if j == n - 1:
            ame_l.append(ame)
            ame = 0
print(max(ame_l))
