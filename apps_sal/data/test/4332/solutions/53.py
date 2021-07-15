n = int(input())
def digitSum(n):
    # 数値を文字列に変換
    s = str(n)
    # １文字ずつ数値化し配列にする。
    array = list(map(int, s))
    # 合計値を返す
    return sum(array)
if n % digitSum(n) == 0:
    print("Yes")
else:
    print("No")
