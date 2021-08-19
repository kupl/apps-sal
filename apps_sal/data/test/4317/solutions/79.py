"""
問題：
    整数 A, B があります。

    A + B, A − B, A ×B
    の中で最大の数を出力してください。
"""
'\n制約：\n入力は全て整数である。\n−100 ≤ A, B ≤ 100\n'
(a, b) = list(map(int, input().split()))
result_list = [a + b, a - b, a * b]
print(max(result_list))
