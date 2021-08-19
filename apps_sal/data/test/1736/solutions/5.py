def read_books(start_index, time, books):
    remaining = time
    current_index = start_index
    books_read = 0
    while True:
        # If we ran out of books
        if current_index == len(books):
            return (books_read, remaining, current_index)

        if remaining >= books[current_index]:
            books_read += 1
            remaining -= books[current_index]
            current_index += 1
        else:
            return (books_read, remaining, current_index)


def max_books(time, books):
    nbooks = [-1] * len(books)

    # Compute if we started with the first book
    nbooks[0] = read_books(0, time, books)

    # compute if we start from the next index
    for i in range(1, len(books)):
        # read what you read previously without the previous book
        min_books = nbooks[i - 1][0] - 1
        max_remaining = nbooks[i - 1][1] + books[i - 1]

        # Try to read some more
        extra = read_books(nbooks[i - 1][2], max_remaining, books)

        # compute the total
        nbooks[i] = (min_books + extra[0], extra[1], extra[2])

    return max(nbooks)[0]


fl = input().split()
t = int(fl[1])
books = [int(item) for item in input().split()]

print((max_books(t, books
                 )))
