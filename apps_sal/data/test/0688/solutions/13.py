
def solution():
    number = input()
    book = {}
    book_of_repeats = {}
    for i in number:
        intermidiate = i
        if intermidiate == "5":
            intermidiate = "2"
        elif intermidiate == "9":
            intermidiate = "6"
        book_of_repeats[intermidiate] = 0
        if intermidiate in book:
            book[intermidiate] += 1
        else:
            book[intermidiate] = 1
    cubs = input()
    for i in cubs:
        intermidiate = i
        if intermidiate == "5":
            intermidiate = "2"
        elif intermidiate == "9":
            intermidiate = "6"
        if intermidiate in book_of_repeats:
            book_of_repeats[intermidiate] += 1
    result = len(cubs) // len(number)
    for i in book:
        intermidiate = book_of_repeats[i] // book[i]
        if intermidiate < result:
            result = intermidiate
    print(result)


def to_mixed_frac(first, second):
    while True:
        for i in range(2, first + 1):
            if first % i == 0 and second % i == 0:
                first //= i
                second //= i
                break
        else:
            break
    return str(first) + "/" + str(second)


def array_to_int(array):
    for i in range(len(array)):
        array[i] = int(array[i])
    return array


def join0(array):
    result = ""
    for i in array:
        result += str(i)
    return result


solution()
