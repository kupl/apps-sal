s = input()
year = int(s[:4])
mo = int(s[5:7])
if year < 2019:
    ans = 'Heisei'
elif year == 2019 and mo <= 4:
    ans = 'Heisei'
else:
    ans = 'TBD'
print(ans)
