
from collections import Counter


def __starting_point():
    n = int(input())
    array = list(map(int, input().split()))
    frequencies = Counter(array)
    target_value, max_frequency = frequencies.most_common(1)[0]
    print(n - max_frequency)

    value_found = False
    for i in range(n):
        elem = array[i]
        if value_found and elem != target_value:
            if elem > target_value:
                print(2, i + 1, i)
            else:
                print(1, i + 1, i)
            array[i] = target_value
        elif elem == target_value:
            value_found = True

    value_found = False
    for i in range(n - 1, -1, -1):
        elem = array[i]
        if value_found and elem != target_value:
            if elem > target_value:
                print(2, i + 1, i + 2)
            else:
                print(1, i + 1, i + 2)
            array[i] = target_value
        elif elem == target_value:
            value_found = True


__starting_point()
