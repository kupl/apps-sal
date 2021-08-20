def main():
    (x, y) = input().split()
    n = int(input())
    f = [int(x), int(y)]
    while len(f) < 6:
        f.append(f[-1] - f[-2])
    print(f[n % 6 - 1] % 1000000007)


main()
