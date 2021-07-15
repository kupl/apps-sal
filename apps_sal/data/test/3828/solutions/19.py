def __starting_point():
    n = int(input())
    line = list(map(int, input().split()))
    book = [0] * n
    for it in line:
        if it > 1:
            if book[it - 2] > 0:
                book[it - 1] = book[it - 2] + 1
            else:
                book[it - 1] = 1
        else:
            book[it - 1] = 1
    print(n - max(book))

__starting_point()
