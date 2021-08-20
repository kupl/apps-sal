input()
s = input() + 'R'
last = 'L'
ix = -1
cnt = 0
for (i, v) in enumerate(s):
    if v == 'R':
        if last == 'L':
            cnt += i - ix - 1
        ix = i
        last = 'R'
    elif v == 'L':
        if last == 'R' and (i - ix) % 2 == 0:
            cnt += 1
        last = 'L'
        ix = i
print(cnt)
