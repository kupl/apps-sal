S = input()
zero = S.count('0')
one = S.count('1')
if zero != 0 and one != 0:
    print(min(zero, one) * 2)
else:
    print(0)
