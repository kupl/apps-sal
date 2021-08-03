n = int(input()) - 1
if n < 2:
    print(-1)
elif n == 2:
    print(210)
else:
    k = str(210 - 10 * pow(10, n - 1, 21))
    print('1' + '0' * (n - len(k)) + k)
