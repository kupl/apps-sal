from itertools import product
s = input()
y = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
yy = list((x + y for (x, y) in product(y, repeat=2)))
mm = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
ans = 'NA'
if (s[0:2] in yy and s[2:4] in mm) and (s[0:2] not in mm or s[2:4] not in yy):
    ans = 'YYMM'
elif (s[0:2] in mm and s[2:4] in yy) and (s[0:2] not in yy or s[2:4] not in mm):
    ans = 'MMYY'
elif (s[0:2] in mm and s[2:4] in yy) and (s[0:2] in yy or s[2:4] in mm):
    ans = 'AMBIGUOUS'
print(ans)
