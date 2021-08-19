s = input()
a = list(input())
a.append('')
cnt = 0
while len(set(a)) == 3:
    for i in range(len(a)):
        if a[i] == 'D':
            if cnt < 0:
                a[i] = ''
            cnt += 1
        if a[i] == 'R':
            if cnt > 0:
                a[i] = ''
            cnt -= 1
for ss in set(a):
    if ss:
        print(ss)
