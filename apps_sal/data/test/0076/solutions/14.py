# python3

def readline():
    return list(map(int, input().split()))


def main():
    n, m, a, b = readline()
    remove = (n % m) * b
    add = (m - n % m) * a
    print(min(add, remove))
    

def __starting_point():
    main()

__starting_point()
