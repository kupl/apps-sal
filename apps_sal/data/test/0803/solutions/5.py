n = int(input())
s = input().strip()
cntx = 0
cntX = 0
for i in range(n):
    if s[i] == 'x':
        cntx += 1
cntX = n - cntx
if cntx > n // 2:
    c = cntx - n // 2
    print(c)
    for i in range(n):
        if s[i] == 'x' and c > 0:
            print('X', end='')
            c -= 1
        else:
            print(s[i], end='')
else:
    c = cntX - n // 2
    print(c)
    for i in range(n):
        if s[i] == 'X' and c > 0:
            print('x', end='')
            c -= 1
        else:
            print(s[i], end='')
