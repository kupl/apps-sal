# joisinoお姉ちゃんは、A op B という式の値を計算したいと思っています。
# ここで、A, Bは整数で、op は、+ または - の記号です。
# あなたの仕事は、joisinoお姉ちゃんの代わりにこれを求めるプログラムを作ることです。

# 制約
# 1 ≦ A, B ≦ 1000000000
# op は、+ または - の記号である。

# 標準入力から A op B を取得する
a, op, b = list(map(str,input().split()))

input_a = int(a)
input_b = int(b)

# opに従い、計算して出力する
result = 0
if op == "+":
    result = input_a + input_b
elif op == "-":
    result = input_a - input_b
else:
    result = "Error"

print(result)

