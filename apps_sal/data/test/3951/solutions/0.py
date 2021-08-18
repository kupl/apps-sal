from fractions import gcd
from random import randint, shuffle
from collections import Counter


def read_numbers():
    return list(map(int, input().split()))


def get_original_array(n, numbers):
    cnt = Counter(numbers)

    array = []
    for new_number in sorted(numbers, reverse=True):
        if cnt[new_number]:
            cnt[new_number] -= 1
            for number in array:
                table_entry = gcd(new_number, number)
                cnt[table_entry] -= 2
            array.append(new_number)
    assert cnt.most_common()[0][1] == 0
    return array


def test(n):
    print(n)
    array = [randint(0, 10**9) for _ in range(n)]
    table = [gcd(a, b) for a in array for b in array]
    shuffle(table)
    print(sorted(array) == sorted(get_original_array(n, table)))


def __starting_point():
    n = int(input())
    numbers = read_numbers()
    print(' '.join(map(str, get_original_array(n, numbers))))


__starting_point()
