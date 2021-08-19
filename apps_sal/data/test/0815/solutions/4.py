def main():
    (a, b, c, d) = list(map(int, input().split()))
    for z in range(1, 501):
        if c <= z and 2 * c >= z and (d <= z) and (2 * d >= z):
            for y in range(z + 1, 501):
                if 2 * b >= y and b <= y and (2 * d < y):
                    for x in range(y + 1, 501):
                        if 2 * a >= x and a <= x and (2 * d < x):
                            print(x)
                            print(y)
                            print(z)
                            return 0
    print(-1)
    return 0


main()
