h, w = map(int, input().split())
table = []
for i in range(h):
    table.append(list(input()))
count = 0
while True:
    if not '#' in table[count]:
        table.pop(count)
        h -= 1
        count = 0
        continue
    if count == h - 1:
        break
    count += 1
count = 0
if h == 1:
    table = [n for n in table[0] if n != '.']
else:
    while True:
        tmp = []
        for i in range(h):
            tmp.append(table[i][count])
        if not '#' in tmp:
            for j in range(h):
                table[j].pop(count)
            w -= 1
            count = 0
            continue
        if count == w - 1:
            break
        count += 1
for row in table:
    print(''.join(row))
