def sum1(x):
    summa = 0
    for i in x:
        summa += int(i)
    return summa


x = input()
c = sum1(x)
result = int(x)
n = len(x) - 1
j = n
for i in range(0, n):
    if x[i] != '0':
        ni = int(x[i]) - 1
        xi = x[0:i] + str(ni) + '9' * j
        j -= 1
        ci = sum1(xi)
        if c < ci:
            c = ci
            result = int(xi)
        elif c == ci and result < int(xi):
            result = int(xi)
    else:
        j -= 1
        continue
print(result)
