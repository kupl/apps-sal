def main():
    n, m, a, b = list(map(int, input().split()))

    if b / m >= a:
        print(n * a)
    else:
        print(min((n//m)*b+(n%m)*a, (n//m+1)*b))

def __starting_point():
    main()


__starting_point()
