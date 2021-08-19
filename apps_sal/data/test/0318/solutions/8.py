(h, m) = map(int, input().split(':'))
a = int(input())
m += h * 60 + a
h = m // 60 % 24
m %= 60
(h, m) = (str(h), str(m))
if len(h) == 1:
    h = '0' + h
if len(m) == 1:
    m = '0' + m
print(h + ':' + m)
