a = int(input())
s = input()
b = []
for c in s:
    if c == 'D':
        b.append(1)
    else:
        b.append(0)
cnt = [0] * 2
while True:
    c = []
    for x in b:
        if cnt[x] > 0:
            cnt[x] -= 1;
        else:
            c.append(x);
            cnt[1 - x] += 1;
    if c == b:
        break
    b = c
if b[0] == 0:
    print('R')
else:
    print('D')

