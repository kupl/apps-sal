def main():
    (N, M) = tuple([int(_x) for _x in input().split()])
    print(N * (N - 1) // 2 + M * (M - 1) // 2)


main()
