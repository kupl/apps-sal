N = input() #1行目のNを取得
N=N.translate(str.maketrans({'1': '9', '9': '1'}))
print(int(N))
