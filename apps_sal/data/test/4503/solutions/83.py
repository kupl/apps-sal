'''
問題：
    アライグマはモンスターと戦っています。

    モンスターの体力は H です。
    アライグマは N 種類の必殺技を使うことができ、
    i 番目の必殺技を使うとモンスターの体力を Ai 減らすことができます。
    必殺技を使う以外の方法でモンスターの体力を減らすことはできません。

    モンスターの体力を 0 以下にすればアライグマの勝ちです。

    アライグマが同じ必殺技を
    2 度以上使うことなくモンスターに勝つことができるなら Yes を、
    できないなら No を出力してください。
'''

'''
制約：
    1 ≦ H ≦ 1000000000
    1 ≦ N ≦ 100000
    1 ≦ Ai ≦ 10000
    入力中のすべての値は整数である。
'''

h, m = list(map(int, input().split()))
a = list(map(int, input().split()))

hissatsu_hp = 0
for i in range(0, m):
    hissatsu_hp += a[i]

result = ""
if hissatsu_hp >= h:
    result = "Yes"
else:
    result = "No"

print(result)
