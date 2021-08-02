S = list(input())
T = list(input())

match = 0

for _ in S:
    i = S.pop()  # 末尾を削除し値を取得
    S.insert(0, i)  # index[0]の位置にiを追加
    ''.join(S)  # リストを結合
    if S == T:
        match += 1
        break

if match == 0:
    print('No')
else:
    print('Yes')
