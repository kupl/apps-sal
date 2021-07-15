n = int(input())
a = ['#' * (n + 2)]
for i in range(1, n+1):
    a.append('#')
    a[i] += input()
    a[i] += '#'
a.append('#' * (n + 2))
o = True
for i in range(1, n + 1):
    for j in range(1, n + 1):
        cnt = 0
        if a[i-1][j] == 'o':
            cnt += 1
        if a[i][j-1] == 'o':
            cnt += 1
        if a[i+1][j] == 'o':
            cnt += 1
        if a[i][j+1] == 'o':
            cnt += 1
        if cnt % 2 != 0:
            o = False
            break
    if o == False:
        break
if o:
    print('YES')
else:
    print('NO')
