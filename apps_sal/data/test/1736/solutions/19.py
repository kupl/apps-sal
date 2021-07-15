__author__ = "runekri3"

n, t = list(map(int, input().split()))
times = list(map(int, input().split()))

max_books = 0
max_books_changed = 0
# last_time = 0
min_time = 0
for i in range(n):
    first_book_time = times[i]
    # last_book_time = times[i+max_books]
    try:
        min_time += times[i + max_books]
    except IndexError:
        break
    # if max_books_changed:
    #     min_time += sum(times[i + max_books - max_books_changed:i + max_books + 1])
    # else:
    #     min_time += times[i + max_books]
    if min_time <= t:
        max_books_changed = 1
        while 1:
            try:
                temp_min_time = min_time + times[i + max_books + max_books_changed]
            except IndexError:
                break
            if temp_min_time <= t:
                min_time = temp_min_time
                max_books_changed += 1
            else:
                min_time = temp_min_time
                break
        max_books += max_books_changed
        pass  # Check if max_books can be increased more
    min_time -= first_book_time

print(max_books)

