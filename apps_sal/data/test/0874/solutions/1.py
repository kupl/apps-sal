num = int(input())
a = list(range(1, num + 1))
if num % 2 != 0:
    print('-1')
else:
    for i in range(num)[::2]:
        (a[i], a[i + 1]) = (a[i + 1], a[i])
    print(' '.join(map(str, a)))
