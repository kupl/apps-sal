n, m = map(int, input().split())

num = [''] * n

flag = 0
for i in range(m):
    s, c = map(int, input().split())
    if num[s - 1] == '' or num[s - 1] == c:
        num[s - 1] = c
    else:
        print(-1)
        break
else:
    if num[0] == '':
        if n > 1:
            num[0] = 1
        else:
            num[0] = 0
    for i in range(1, n):
        if num[i] == '':
            num[i] = 0
    if n > 1 and num[0] == 0:
        print(-1)
    else:
        print(''.join(map(str, num)))
