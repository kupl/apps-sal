a, b = map(int, input().split())

# 整数a をb回繰り返してできる文字列と 整数b をa回繰り返してできる文字列のうち、
# 辞書順で小さい方を出力せよ。
# (2つの文字列が等しいときは、そのうちどちらかを出力せよ。)

if a > b:
    b = str(b)
    print(b * a)
else:
    a = str(a)
    print(a * b)
