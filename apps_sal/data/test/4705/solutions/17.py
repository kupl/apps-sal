input_num = int(input())

# x - y （円）を計算し出力する。
x = input_num * 800  # x：今までに払った金額
y = int(input_num / 15) * 200  # y：レストランからもらった金額
result = x - y  # 差額

print(result)
