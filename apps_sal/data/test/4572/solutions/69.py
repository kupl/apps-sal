S = list(input())
a = list('abcdefghijklmnopqrstuvwxyz')
for i in S:
    if i in a:
        a.remove(i)
if a:
    print(a[0])
else:
    print('None')
