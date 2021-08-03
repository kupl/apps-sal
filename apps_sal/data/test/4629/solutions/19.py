import itertools

LIMIT = 9

powers = [i for i in range(LIMIT)]
perms = []
items = []

numbers = []

for i in range(1, LIMIT + 1):
    perms += itertools.combinations(powers, i)

for i in perms:
    r = 0

    for j in i:
        r += pow(3, j)

    numbers.append(r)

numbers.append(3**9)
numbers.sort()


def find(l, r, item):
    mid = l + (r - l) // 2

    if r >= l:
        if numbers[mid] == item:
            return item

        if numbers[mid] > item:
            return find(l, mid - 1, item)

        else:
            return find(mid + 1, r, item)
    else:
        return numbers[l]


q = int(input())
l_numbers = len(numbers)

for _ in range(q):
    n = int(input())

    print(find(0, l_numbers, n))
