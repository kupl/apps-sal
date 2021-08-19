# 英小文字 c が与えられるので、 c が母音であるか判定してください。ここで、英小文字のうち母音は a、e、i、o、uの 5 つです。

c = input()
if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
    print('vowel')
else:
    print('consonant')
