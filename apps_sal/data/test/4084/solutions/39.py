def main():
    N, A, B = tuple([int(_x) for _x in input().split()])
    turn = A + B
    iteration = (N // turn)
    rest = N - iteration * turn
    restb = min(A, rest)
    print((A*iteration+restb))


main()

