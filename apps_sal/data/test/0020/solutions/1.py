def f(x, y):
    xx = str(x)
    if len(xx) == 1:
        xx = '0' + xx
    yy = str(y)
    if len(yy) == 1:
        yy = '0' + yy
    return yy[::-1] != xx


def read():
    return map(int, input().split(':'))


(a, b) = read()
cnt = 0
while f(a, b):
    b += 1
    if b == 60:
        a += 1
        b = 0
    if a == 24:
        a = 0
    cnt += 1
print(cnt)
