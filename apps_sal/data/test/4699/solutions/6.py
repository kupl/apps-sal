total, k = list(map(int, input().split()))

d = list(map(int, input().split()))


def total_to_digits(total):
    return list(map(int, list(str(total))))


def find_lowest_denomination(total, d):
    res = None
    for i in range(total, 99999):
        digits = list(total_to_digits(i))
        if not (set(digits) & set(d)):
            print(i)
            return


find_lowest_denomination(total, d)
