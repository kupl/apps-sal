def main():
    n, a, b = map(int, input().split())
    print((a + b - 1 + n) % n + 1)


main()
