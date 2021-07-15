y,m,d = map(int,input().split('/'))
if m <= 4:
    ans = 'Heisei'
elif m > 4:
    ans = 'TBD'
print(ans)
