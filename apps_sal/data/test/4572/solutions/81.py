s = str(input())
alp = set('abcdefghijklmnopqrstuvwxyz')
s = set(s)
if len(s & alp) == 26:
    ans = 'None'
else:
    lis = list(alp - s)
    lis.sort()
    ans = lis[0]
print(ans)
