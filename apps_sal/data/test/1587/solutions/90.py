n = int(input())
c = input()

# 入れ替えても色を変えてもコストは変わらない
# 最も左にあるWと最も右にあるRを入れ替え、RRR・・・WWW・・・を目指す
# 初期局面と最終局面を比較すると、入れ替えるべき石の総数が分かる

r_cnt = c.count('R')
print(c[:r_cnt].count('W'))
