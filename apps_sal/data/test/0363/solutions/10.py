def __starting_point():
    n_books = int(input())
    x = 0
    length = 1
    while n_books > 10**length - 1:
        x += (10**length - 10**(length - 1)) * length
        length += 1
    x += (n_books - 10**(length - 1) + 1) * length
    print(x)


__starting_point()
