S = input()
(y, m, d) = S.split('/')
(y, m, d) = (int(y), int(m), int(d))
if y == 2019:
    if m <= 4:
        if d <= 30:
            ans = 'Heisei'
        else:
            ans = 'TBD'
    else:
        ans = 'TBD'
elif y < 2019:
    ans = 'Heisei'
else:
    ans = 'TBD'
print(ans)
