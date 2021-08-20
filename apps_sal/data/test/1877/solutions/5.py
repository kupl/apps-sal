n = int(input())
st = input()
isUp = st[0] == 'U'
x = 0
y = 0
if st[0] == 'U':
    y += 1
else:
    x += 1
c = 0
for i in range(1, n):
    if isUp and x == y and (st[i] == 'R'):
        c += 1
        isUp = False
    elif not isUp and x == y and (st[i] == 'U'):
        c += 1
        isUp = True
    if st[i] == 'U':
        y += 1
    else:
        x += 1
print(c)
