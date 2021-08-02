s = int(input())
a = [s]


def func(n):
    if n % 2 == 0:
        a.append(n // 2)
    elif n % 2 == 1:
        a.append(3 * n + 1)


i = 1
while True:
    func(a[-1])
    i += 1
    if a.count(a[-1]) == 2:
        break
    else:
        pass


print(i)
