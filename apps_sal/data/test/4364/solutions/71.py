s = str(input())
ans = ['YYMM', 'MMYY', 'AMBIGUOUS', 'NA']
# print(s[:2],s[-2:])
if (0 == int(s[:2]) or 13 <= int(s[:2])) and (0 == int(s[-2:]) or 13 <= int(s[-2:])):
    print((ans[3]))
if 0 < int(s[:2]) <= 12 and 0 < int(s[-2:]) <= 12:
    print((ans[2]))
elif 0 < int(s[:2]) <= 12:
    print((ans[1]))
elif 0 < int(s[-2:]) <= 12:
    print((ans[0]))
