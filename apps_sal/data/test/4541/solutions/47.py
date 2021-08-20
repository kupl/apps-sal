"""
問題：
    英小文字 cが与えられるので、c が母音であるか判定してください。
    ここで、英小文字のうち母音は a、e、i、o、uの 5つです。
"""
'\n制約：\n    cは英小文字である。\n'
c = str(input())
vowel_words = ('a', 'e', 'i', 'o', 'u')
result = 'ret'
if c in vowel_words:
    result = 'vowel'
else:
    result = 'consonant'
print(result)
