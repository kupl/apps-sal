s = int(input())
a = [s]
i = 0
while True:
    i = i + 1
    if a[i - 1] % 2 == 0:
        n = a[i - 1] // 2
    else:
        n = 3 * a[i - 1] + 1
    if n in a:
        print((i + 1))
        break
    a.append(n)
