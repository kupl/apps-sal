h, m = map(int, input().split(':'))
n = int(input())
m, h = (m + n) % 60, (h + (m + n) // 60) % 24
if h < 10:
    h = '0' + str(h)
if m < 10:
    m = '0' + str(m)
print(h, m, sep=':')
