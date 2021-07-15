# シカのAtCoDeerくんとTopCoDeerくんが「正直者か嘘つきか」ゲームをしています。
# このゲームでは、正直者は常にほんとうのことを言い、嘘つきは常に嘘を言います。
# 文字 a と b が入力として与えられます。
# これらはそれぞれ H か D のどちらかです。
# a=H のとき、AtCoDeerくんは正直者です。
# a=D のとき、AtCoDeerくんは嘘つきです。
# b=H のとき、AtCoDeerくんは「TopCoDeerくんは正直者だ」と発言しています。
# b=D のとき、AtCoDeerくんは「TopCoDeerくんは嘘つきだ」と発言しています。
#
# これらから判断して、TopCoDeerくんが正直者かどうか判定してください。

# 制約
# a='H' または 'D'
# b='H' または 'D'


# 標準入力から文字列 a と b を取得する
input_a, input_b = list(map(str,input().split()))

reslut = "ret"

# TopCoDeerくんが正直者かどうか判定し、結果を出力する。
# ※ 正直者=="H"、嘘つき=="D"
if input_a == "H":  # AtCoDeerくんが正直者の場合
    if input_b == "H":
        result = "H"
    elif input_b == "D":
        result = "D"
elif input_a == "D":    # AtCoDeerくんが嘘つき者の場合（条件増えた時ようにelifにした）
    if input_b == "H":
        result = "D"
    elif input_b == "D":
        result = "H"
else:
    reslut = "I don't Know."

print(result)



