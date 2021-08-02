k = int(input())


def f(num):
    return num / sum(map(int, list(str(num))))


order = 0
sunuke = 1
for i in range(k):
    print(sunuke)
    sunuke += 10**order
    if f(sunuke + 10**(order + 1)) < f(sunuke + 10**order):
        order += 1
