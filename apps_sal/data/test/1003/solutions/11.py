def main():
    (n, m) = map(int, input().split(' '))
    d = 0
    while True:
        d += 1
        n -= 1
        if d % m == 0:
            n += 1
            pass
        if n == 0:
            break
            pass
        pass
    print(d)
    pass


main()
