a, b = list(map(int, input().split()))

# 文字列として扱う
A = str(a)
B = str(b)

aaa = A * b
bbb = B * a

# 辞書順で小さい方を出力
lists = sorted([aaa, bbb])
print((lists[0]))

