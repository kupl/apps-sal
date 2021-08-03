"""
ABC049 A - 居合を終え、青い絵を覆う
https://atcoder.jp/contests/abc049/tasks/abc049_a
"""

c = input()
boin = ['a', 'e', 'i', 'o', 'u']
if c in boin:
    print('vowel')
else:
    print('consonant')
