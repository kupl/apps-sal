k, x = map(int, input().split())
number = []
# xから前ｋ-1個、後k-1個の数をリストに加える
for i in range(x - (k - 1), x + (k - 1) + 1):
    number.append(i)
# リストの要素を文字列型に変換
number_str = [str(n) for n in number]
# リストの要素をjoinで連結
num = " ".join(number_str)
print(num)
