"""
問題：
    英小文字からなる文字列 s が与えられます。
    前から数えて奇数文字目だけ抜き出して作った文字列を出力してください。
    ただし、文字列の先頭の文字を1文字目とします。
"""
'\n制約：\n    s の各文字は英小文字\n    1 ≦ |s| ≦ 100000\n'
s = str(input())
i = 1
result = ''
for i in range(len(s) + 1):
    if i % 2 == 0:
        pass
    else:
        result += s[i - 1]
print(result)
