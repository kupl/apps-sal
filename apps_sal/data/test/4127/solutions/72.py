# coding=utf-8

def __starting_point():
    A, B = input().split()
    A = int(A)
    B = float(B)
    B = int(B*100+0.5)

    print((A*B//100))

__starting_point()
