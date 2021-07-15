from fractions import Fraction

s = input()

tmp_1 = Fraction(len(s) - 1, 2)
tmp_2 = Fraction(len(s) + 3, 2)

a = s[0: int(tmp_1)]
b = s[int(tmp_2) - 1: int(len(s))]

print('Yes' if a == b else 'No')
