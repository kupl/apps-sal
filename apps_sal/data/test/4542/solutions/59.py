# 81 C - 一次元リバーシ
S = input()
S = S + '1'  # 番兵

# 連続する文字をカウント
cnt = []
conti = 1
for i in range(1, len(S)):
    if S[i - 1] == S[i]:
        conti += 1
    else:
        cnt.append(conti)
        conti = 1
print(len(cnt) - 1)
