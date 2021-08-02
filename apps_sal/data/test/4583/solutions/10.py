import itertools
L = ['+', '-']
s = list(input())
for l in itertools.product(L, repeat=3):
    if 7 == eval(s[0] + l[0] + s[1] + l[1] + s[2] + l[2] + s[3]):
        print(s[0] + l[0] + s[1] + l[1] + s[2] + l[2] + s[3] + '=7')
        break
