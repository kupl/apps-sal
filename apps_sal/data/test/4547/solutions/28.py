'''
問題：
    今、日本は 9 月 9 日です。
    二桁の整数 N が与えられるので、十進法で N に 9 が含まれるか答えてください。
'''
'''
制約：
10 ≦ N ≦ 99
'''

# 標準入力から N を取得する
n = int(input())

result = ""
if n % 10 == 9: # 1の位が 9
    result = "Yes"
elif 90 <= n % 100 < 100:   # 10の位が 9
    result = "Yes"
else:
    result = "No"

print(result)

