x = int(input())


def f():
    for i in range(x, 10**10):
        c = 0
        for j in range(2, i):
            if i % j != 0:
                c += 1
                if c == i - 2:
                    return i
            else:
                break


if x == 2:
    print(2)
else:
    print(f())
