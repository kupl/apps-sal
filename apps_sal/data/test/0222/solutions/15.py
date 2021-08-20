n = input()
le = len(n)
m = le
for i in range(1, 2 ** le):
    i = bin(i)[2:]
    s = ''
    c = le
    for j in range(len(i)):
        if i[-1 - j] == '1':
            s = n[le - 1 - j] + s
            c -= 1
    if s[0] == '0':
        continue
    s = int(s)
    if int(s ** (1 / 2)) ** 2 == s:
        m = min(m, c)
if m == le:
    print(-1)
else:
    print(m)
