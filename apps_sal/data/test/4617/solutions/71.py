'''
問題：
    縦 2 マス、横 3 マスのマス目が与えられます。
    上から i 行目、左から j 行目のマスの色は、Cij で表されます。

    このマス目を 180 度回転させたとき、
    元のマス目と一致するなら YES を、そうでないなら NO を出力するプログラムを作成してください。
'''

'''
制約：
    Cij（1 ≦ i ≦ 2、 1 ≦ j ≦ 3）は英小文字である。
'''

cij = str(input())
cji = str(input())

reverse_cij = cij[2] + cij[1] + cij[0]

result = ""
if cji == reverse_cij:
    result = "YES"
else:
    result = "NO"

print(result)
