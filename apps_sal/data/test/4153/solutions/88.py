S = str(input())
x = len(S)
if '0' in S:
    y0 = S.count('0')
else:
    y0 = 0
if '1' in S:
    y1 = S.count('1')
else:
    y1 = 0

d = abs(y0 - y1)
print((x - d))
