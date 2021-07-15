# test = iter('''0
# 1 2
# '''.splitlines())
#
#
# def input():
#     return next(test)


def int_input():
    return int(input())


def ints_input():
    return (int(x) for x in input().split())


t=int_input()
for _ in range(t):
    n,k=ints_input()
    if (n&1) == 0:
        print(n+k+k)
    else:
        for i in range(3, n+1, 2):
            if n % i == 0:
                print(n+i+2*(k-1))
                break
