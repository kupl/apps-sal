l = int(input())
a = []
ans = 0
b = []
for i in range(l + 5):
    a.append(0)
    b.append(0)
temp = 1
ii = 1
a[0] = 1
b[0] = 1
g = 2 ** 32 - 1
over = 0
for i in range(l):
    x = list(input().split())
    if x[0] == 'add':
        ans += b[ii - 1] * 1
    elif x[0] == 'for':
        b[ii] = int(x[1]) * b[ii - 1]
        a[ii] = int(x[1])
        if b[ii] > g:
            b[ii] = g + 2
        ii += 1
    elif x[0] == 'end':
        temp = b[ii - 1] // a[ii - 1]
        ii -= 1
    if ans > g:
        over = 1
        break
if over == 1:
    print('OVERFLOW!!!')
else:
    print(ans)
