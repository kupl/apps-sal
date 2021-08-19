s = int(input())
a = [0, s]
for n in range(2, 10 ** 6 + 1):
    if a[n - 1] % 2 == 0:
        an = a[n - 1] // 2
    else:
        an = a[n - 1] * 3 + 1
    if an in a:
        m = n
        break
    a.append(an)
print(m)
