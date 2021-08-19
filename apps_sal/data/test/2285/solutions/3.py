n = int(input())
adrs = [input().split(':') for i in range(n)]
res = []
for ad in adrs:
    new_ad = ''
    ind = 0
    for s in ad:
        if s:
            new_ad += '0' * (4 - len(s)) + s + ' '
        elif s == '::':
            res.append('0000 ' * 8)
            break
        elif not s and ind == 0:
            new_ad += '0000 ' * (8 - len(ad) + ad.count(''))
            ind = 1
    res.append(new_ad)
for x in res:
    print(x.replace(' ', ':')[:39])
