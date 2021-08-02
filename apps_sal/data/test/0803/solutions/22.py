n = int(input())
a = list(input())
xa = a.count('x')
xb = a.count('X')
xc = 'x' if xb > xa else 'X'
result = int(abs(n / 2 - xa))
print(result)
for i in a:
    if result == 0:
        break
    if i != xc:
        a[a.index(i)] = xc
        result -= 1
print("".join(a))
