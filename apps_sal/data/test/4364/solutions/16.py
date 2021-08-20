s = input()
s1 = s[:2]
s2 = s[2:4]
r = int(s2)
l = int(s1)
if 1 <= r <= 12 and 1 <= l <= 12:
    print('AMBIGUOUS')
elif (r > 12 or r == 0) and 1 <= l <= 12:
    print('MMYY')
elif (l >= 12 or l == 0) and 1 <= r <= 12:
    print('YYMM')
else:
    print('NA')
