# cが母音であるか判定する。
# 母音はa,e,i,o,uの５つ
c = input('')

vowels = ['a', 'e', 'i', 'o', 'u']

if c in vowels:
    print('vowel')
else:
    print('consonant')
