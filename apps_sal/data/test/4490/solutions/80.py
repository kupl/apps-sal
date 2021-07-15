# A,Double Helix
# AtCoder 星には四種類の塩基 A, C, G, T が存在し、A と T、C と G がそれぞれ対になります。
# 文字 bが入力されます。これは A, C, G, T のいずれかです。塩基bと対になる塩基を表す文字を出力するプログラムを書いてください。

# bは文字 A, C, G, T のいずれかである。

b = input()

# 塩基bと対になる塩基を表す文字を出力せよ。

if b == "A":
    print("T")
elif b == "T":
    print("A")
elif b == "C":
    print("G")
elif b == "G":
    print("C")
