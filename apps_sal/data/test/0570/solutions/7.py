import sys

def solve():
    a, b = map(int, input().split())

    for i in range(10**9):
        if 2*i + 1 > a:
            print('Vladik')
            return
        else:
            a -= 2*i + 1

        if 2*i + 2 > b:
            print('Valera')
            return
        else:
            b -= 2*i + 2

def __starting_point():
    solve()
__starting_point()
