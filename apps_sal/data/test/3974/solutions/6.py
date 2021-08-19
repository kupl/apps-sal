def puts(s):
    print(s, end='')


s = input()
a = mi = ma = 0
for c in s:
    if c == '+':
        a = a + 1
        ma = max(ma, a)
    else:
        a = a - 1
        mi = min(mi, a)
print(ma - mi)
