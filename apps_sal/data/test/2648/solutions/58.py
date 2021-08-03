
def resolve():
    N = int(input())
    A = list(map(int, input().split(" ")))
    import collections
    cnter = collections.Counter(A)
    # print(cnter)
    evens = 0
    for i in list(cnter.values()):
        if i % 2 == 0:
            evens += 1
    print((len(cnter) - 1 if evens % 2 == 1 else len(cnter)))


def __starting_point():
    resolve()


__starting_point()
