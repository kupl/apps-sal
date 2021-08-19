l = int(input())


def f(n):
    return n / sum(list(map(int, list(str(n)))))


a = []
for i in range(1, 16):
    if i <= 3:
        for j in range(1, 10):
            a.append((j + 1) * 10 ** (i - 1) - 1)
    elif i <= 12:
        for j in range(1, 10):
            b = [j * 10 ** (i - 1) + (k + 1) * 10 ** (i - 2) - 1 for k in range(10)]
            for k in range(9)[::-1]:
                if f(b[k]) > f(b[k + 1]):
                    b.pop(k)
            a += b
    else:
        for j in range(1, 10):
            b = [j * 10 ** (i - 1) + (k + 1) * 10 ** (i - 3) - 1 for k in range(100)]
            for k in range(99)[::-1]:
                if f(b[k]) > f(b[k + 1]):
                    b.pop(k)
            a += b
for i in range(l):
    print(a[i])
