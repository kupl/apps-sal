a = int(input())
for x in range(a):
    prev = ''
    next = ''
    str = input()
    res = []
    ch = 0
    for i in range(len(str)):
        if str[i] == prev:
            print(-1)
            ch = 1
            break
        if i + 1 != len(str):
            next = str[i + 1]
        if str[i] == '?':
            if 'a' != prev and 'a' != next:
                res.append('a')
                prev = 'a'
            elif 'b' != prev and 'b' != next:
                res.append('b')
                prev = 'b'
            elif 'c' != prev and 'c' != next:
                res.append('c')
                prev = 'c'
        if str[i] == 'a' or str[i] == 'b' or str[i] == 'c':
            prev = str[i]
            res.append(prev)
    if ch == 0:
        print(''.join(y for y in res))
