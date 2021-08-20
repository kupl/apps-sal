(n, m) = list(map(int, input().split()))
empthy = '.' * m
last = ''
mistake = False
for i in range(n):
    s = input()
    if s != empthy:
        if last == '':
            last = s
        elif last != s:
            mistake = True
            break
if mistake:
    print('NO')
else:
    print('YES')
