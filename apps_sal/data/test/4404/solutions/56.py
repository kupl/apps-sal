s = input()
month = int(s[5:7])
if month < 4:
    ans = 'Heisei'
elif month == 4:
    day = int(s[8:])
    if day <= 30:
        ans = 'Heisei'
else:
    ans = 'TBD'
print(ans)
