def main():
    n = int(input())
    sm = 0
    for i in range(1, n // 2):
        sm += 2 ** i
    for i in range(n // 2, n):
        sm -= 2 ** i
    sm += 2 ** n
    print(sm)


def __starting_point():
    t = int(input())
    for i in range(t):
        main()


__starting_point()
