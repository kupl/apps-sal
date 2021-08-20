def f(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


s = int(input())
a = []
for i in range(1000000):
    if i == 0:
        a.append(s)
    elif f(a[-1]) in a:
        print(i + 1)
        break
    else:
        a.append(f(a[-1]))
