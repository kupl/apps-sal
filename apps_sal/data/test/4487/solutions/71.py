# 数値を取得
word_list = input().split()
w_cnt = len(word_list)

# 語頭語尾の抽出
s_list = []
e_list = []
for cnt in range(0,w_cnt,1):
    s_list.append(word_list[cnt][0])
    e_list.append(word_list[cnt][-1])

# 成立してるか検査後結果を出力
judge = "YES"
for cnt in range(1,w_cnt,1):
    if s_list[cnt] != e_list[cnt-1]:
        judge = "NO"
print(judge)
