'''
問題：
    英小文字 cが与えられるので、c が母音であるか判定してください。
    ここで、英小文字のうち母音は a、e、i、o、uの 5つです。
'''

'''
制約：
    cは英小文字である。
'''

# 標準入力から c を取得する
c = str(input())

vowel_words = ('a', 'e', 'i', 'o', 'u')

result = 'ret'
if c in vowel_words:
    result = 'vowel'
else:
    result = 'consonant'

print(result)
