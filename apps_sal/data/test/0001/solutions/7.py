n = int(input())


def f(numb):
    lst = [numb]
    cap = 10

    while numb // cap > 0:
        lst.append((numb // cap - 1) * cap + cap - 1)
        cap *= 10

    return lst


def g(numb):
    lst = []
    while numb != 0:
        lst.append(numb % 10)
        numb //= 10

    return lst


maximum = max([sum(g(i)) for i in f(n)])

maximum = [i for i in f(n) if maximum == sum(g(i))]

print(max(maximum))
