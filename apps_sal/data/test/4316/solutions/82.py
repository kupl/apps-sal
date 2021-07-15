s = input()
sl = []
for i in s:
    if i not in sl:
        sl.append(i)
if len(sl) == 2:
    n = 0
    for i in s:
        if i == sl[0]:
            n += 1
    if n == 2:
        print('Yes')
else:
    print('No')
