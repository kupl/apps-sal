def main():
    (n, k) = list(map(int, input().split()))
    while n != 0:
        if k == 2 ** (n - 1):
            print(n)
            return
        else:
            k = k % 2 ** (n - 1)
        n -= 1


main()
