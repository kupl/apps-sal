input()
a = [int(i) for i in input().split(' ')]
r = 'NO'
mi = 0
for i in a:
    if mi == 1:
        i -= mi
        mi = 0
    if i < 0:
        break
    elif i == 0:
        continue
    elif i % 2 != 0:
        mi = 1
else:
    if mi == 1:
        r = 'NO'
    else:
        r = 'YES'
print(r)
