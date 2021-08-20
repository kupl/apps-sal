n = int(input())


def f(a, b):
    (a, b) = (len(str(a)), len(str(b)))
    return max(a, b)


flist = []
a = int(n ** 0.5)
for i in range(1, a + 1):
    if n % i == 0:
        j = int(n / i)
        tmp = f(i, j)
        flist.append(tmp)
print(min(flist))
