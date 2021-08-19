len = int(input())
line = input().split(' ')
cnt = 1
i = 1
while i < len:
    if line[i] != line[i - 1]:
        cnt = cnt + 1
    i = i + 1
need_len = len // cnt
if need_len * cnt != len:
    print('NO')
else:
    i = 0
    while i < len:
        size = 0
        if int(line[i]) == 1:
            while i < len and int(line[i]) == 1:
                i = i + 1
                size = size + 1
        else:
            while i < len and int(line[i]) == 0:
                i = i + 1
                size = size + 1
        if size != need_len:
            print('NO')
            i = len + 100
    if i - 10 < len:
        print('YES')
