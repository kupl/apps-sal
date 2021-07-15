a,b = map(int,input().split())
# a,bを文字列化
a_str = str(a)
b_str = str(b)
# a*bとb*aを昇順でならべてリスト化
ab_list = sorted([a_str * b, b_str * a])
# リストの1番目を出力
print(ab_list[0])
