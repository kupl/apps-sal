m = list(input())

d = {}

for c in m:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

cnt = 0

for c in d:
    if d[c] % 2:
        cnt += 1

if not cnt:
    print('First')
else:
    if cnt % 2:
        print('First')
    else:
        print('Second')
