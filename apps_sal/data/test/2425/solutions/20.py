def find_log(number):
    counter = 1
    while number > 1:
        number = number // 2
        counter += 1
    return counter


def __starting_point():

    q = int(input())
    a = [0 for i in range(q)]
    for i in range(q):
        a[i] = int(input())

    NUMS = [0 for i in range(24)]
    for i in range(24):
        NUMS[i] = 2**(i + 2) - 1
    PRIMES = [3, 7, 3, 31, 3, 127, 3, 7, 3, 23, 3, 8191, 3, 7, 3, 131071, 3, 524287, 3, 7, 3, 47, 3, 31]

    for i in range(q):
        if a[i] not in NUMS:
            k = find_log(a[i])
            print(2**k - 1)
        else:
            index = -1
            found = False
            while not found:
                index += 1
                if NUMS[index] == a[i]:
                    found = True
            print(int(a[i] / PRIMES[index]))


__starting_point()
