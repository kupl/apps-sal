# 入力を受け取る
a,b = input().split()

#aをb個、bをa個並べたものを作る
str_a = a*int(b)
str_b = b*int(a)

#aとbを比較して、辞書順に小さい方を出力する
print(str_a if str_a < str_b else str_b)
