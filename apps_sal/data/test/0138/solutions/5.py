def main():
    try:
        while True:
            (n, a, b, c) = list(map(int, input().split()))
            result = 1e+20
            for ia in range(4):
                for ib in range(4):
                    for ic in range(4):
                        x = n + ia + (ib << 1) + ic * 3
                        if x & 3 == 0:
                            result = min(result, ia * a + ib * b + ic * c)
            print(result)
    except EOFError:
        pass


main()
