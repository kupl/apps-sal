input()
a = list(input()) + ['']
cnt = 0
while len(set(a)) == 3:
    for (i, v) in enumerate(a):
        if v == 'D':
            if cnt < 0:
                a[i] = ''
            cnt += 1
        if v == 'R':
            if cnt > 0:
                a[i] = ''
            cnt -= 1
for ss in set(a):
    if ss:
        print(ss)
