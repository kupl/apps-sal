import math
def read(): return map(int, input().split())


def codeforce1149A():
    n = int(input())
    p = list(read())
    if len(p) == 1:
        print(p[0])
        return
    odd, even = 0, 0
    for i in p:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd == 0:
        for i in p:
            print(i, end=' ')
    elif even == 0:
        for i in p:
            print(i, end=' ')
    else:
        print(2, 1, end=' ')
        even -= 1
        odd -= 1
        for _ in range(even):
            print(2, end=" ")
        for _ in range(odd):
            print(1, end=' ')


def __starting_point():
    codeforce1149A()


__starting_point()
