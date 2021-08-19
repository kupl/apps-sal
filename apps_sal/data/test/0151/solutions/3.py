st = input()
k = 0
i = 0
while i < len(st):
    if not st[i] in ['a', 'e', 'i', 'o', 'u']:
        if k < 3:
            k += 1
    else:
        k = 0
    if k == 3:
        if not st[i] == st[i - 1] == st[i - 2]:
            st = st[:i] + ' ' + st[i:]
            k = 1
            i += 1
    i += 1
print(st)
