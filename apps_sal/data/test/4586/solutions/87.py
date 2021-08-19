'''
問題：
    1118 のような、3 つ以上の同じ数字が連続して並んだ
    4 桁の整数を 良い整数 とします。

    4 桁の整数N が与えられるので、N が 良い整数 かどうかを答えてください。
'''

'''
制約：
    1000 ≦ N ≦ 9999
    入力は整数からなる
'''

# 標準入力から N を取得する
n = int(input())
list_n = list(str(n))

result = ""

if (list_n[0] == list_n[1]) and (list_n[1] == list_n[2]):
    result = "Yes"
elif (list_n[1] == list_n[2]) and (list_n[2] == list_n[3]):
    result = "Yes"
else:
    result = "No"

print(result)
