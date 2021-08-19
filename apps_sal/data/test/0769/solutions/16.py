from decimal import *
(a, b, c) = map(int, input().split())
getcontext().prec = 100000
dec = Decimal(a) / Decimal(b)
t = -1
s = str(dec)
y = -1
for i in range(100000):
    st = '0'
    if i < len(s):
        st = s[i]
    if st == '.':
        y = i
    if st == str(c):
        if y >= 0:
            t = i - y
            break
print(t)
