s = [int(i) for i in input().split('/')]
ans = 'TBD'
if s[0] <= 2018:
    ans = 'Heisei'
elif s[0] == 2019 and s[1] <= 4:
    ans = 'Heisei'
print(ans)
