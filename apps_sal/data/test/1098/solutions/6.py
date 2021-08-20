n = int(input())
x = []
for i in range(n):
    (a, b) = map(int, input().split(':'))
    x.append(a * 60 + b)
x = sorted(x)
x.append(x[0] + 24 * 60)
m = 0
for i in range(n):
    m = max(m, x[i + 1] - x[i] - 1)
x = str(m // 60)
y = str(m % 60)
if len(x) < 2:
    x = '0' + x
if len(y) < 2:
    y = '0' + y
s = x + ':' + y
print(s)
