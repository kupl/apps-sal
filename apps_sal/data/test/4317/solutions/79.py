'''
問題：
    整数 A, B があります。

    A + B, A − B, A ×B
    の中で最大の数を出力してください。
'''

'''
制約：
入力は全て整数である。
−100 ≤ A, B ≤ 100
'''

# 標準入力から A, B の値を取得する
a, b = list(map(int, input().split()))

result_list = [a + b, a - b, a * b]  # 結果格納用リスト

print((max(result_list)))
