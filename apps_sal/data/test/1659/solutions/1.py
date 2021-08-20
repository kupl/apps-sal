d = 0
(a, b) = list(map(int, input().split(' ')))
ic = b
for i in range(a):
    (x, y) = list(map(str, input().split(' ')))
    if x == '+':
        ic += int(y)
    elif int(y) > ic:
        d += 1
    else:
        ic -= int(y)
print(ic, d)
