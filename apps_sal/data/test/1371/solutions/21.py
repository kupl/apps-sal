def hoge(n):
    if n == 1 or n == 2:
        return 0
    if n == 3:
        return 1
    t = [0, 0, 1]
    for i in range(4, n + 1):
        a = t[-1] + t[-3]
        a = a % (10 ** 9 + 7)
        t.append(a)
    return t[-1]


n = int(input())
print(hoge(n))
