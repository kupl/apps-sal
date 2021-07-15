x = int(input())
answer_year = 0
deposit = 100

# 預金額がｘ円以上になるまで繰り返し
while deposit < x:
    # 金利の小数点以下は切り捨て
    deposit = deposit + (deposit // 100)
    # 年数をカウントアップ
    answer_year += 1

print(answer_year)
