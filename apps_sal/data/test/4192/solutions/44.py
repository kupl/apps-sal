(d, t, s) = map(int, input().split(' '))
temp = d / s
if temp <= t:
    print('Yes')
else:
    print('No')
