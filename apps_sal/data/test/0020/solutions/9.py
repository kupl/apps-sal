(h, m) = [int(i) for i in input().split(':')]
c = 0
while True:
    s = str(h).rjust(2, '0') + str(m).rjust(2, '0')
    if s == s[::-1]:
        break
    c += 1
    m += 1
    if m >= 60:
        m %= 60
        h += 1
    if h == 24:
        h = 0
print(c)
