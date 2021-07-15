def digits_until_block_(n):
    result = 0
    for bas in range(1, 30):
        minimum = int(10 ** (bas - 1))
        maximum = int((10 ** bas) - 1)
        if n < maximum:
            maximum = n
        if maximum < minimum:
            break
        result += sum_between(n - maximum + 1, n - minimum + 1) * bas
    return result


def digits_until_(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return digits_until_block_(n) - digits_until_block_(n - 1)


def sum_between(x, y):
    try:
        assert (x <= y)
    except AssertionError:
        print(x, y)
    return ((x + y) * (y - x + 1)) // 2


def solve(q):
    left = 1
    right = 10000000000
    while left < right:
        mid = (left + right) // 2
        if digits_until_block_(mid) < q:
            left = mid + 1
        else:
            right = mid
    q = q - digits_until_block_(left - 1)
    left = 1
    right = 10000000000
    while left < right:
        mid = (left + right) // 2
        if digits_until_(mid) < q:
            left = mid + 1
        else:
            right = mid
    q = q - digits_until_(left - 1)
    return str(left)[q - 1]


q = int(input(""))
q_list = []
for _ in range(q):
    q_list.append(int(input("")))
for query in q_list:
    print(solve(query))

