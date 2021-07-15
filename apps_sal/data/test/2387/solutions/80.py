from itertools import chain
import sys

def main():
    N = int(input())
    # TLEs were caused mostly by slow input (1s+)
    # S = list(input() for _ in range(N))
    S = sys.stdin.read().split('\n')
    print((solve(S)))

def get_count(args):
    s, result = args # messy input to work with map.
    cum_sum = 0
    for c in s:
        if c == ')':
            cum_sum -= 1
        else:
            cum_sum += 1
        result[0] = max(result[0], -cum_sum)
    result[1] = result[0] + cum_sum
    return result

# Made-up name, don't remember what to call this. Radix-ish
def silly_sort(array, value_min, value_max, get_value):
    if len(array) == 0:
        return
    cache = [None for _ in range(value_max - value_min + 1)]
    for elem in array:
        # Assume elem[0] is the value
        value = get_value(elem) - value_min
        if cache[value] is None:
            cache[value] = []
        cache[value].append(elem)
    for values in cache:
        if values is None:
            continue
        for value in values:
            yield value

def solve(S):
    counts = [[0,0] for _ in range(len(S))]
    counts = list(map(get_count, list(zip(S,counts))))
    first_group = []
    second_group = []
    min_first_group = float('inf')
    max_first_group = 0
    min_second_group = float('inf')
    max_second_group = 0

    for c in counts:
        if c[0] - c[1] <= 0:
            first_group.append(c)
            max_first_group = max(max_first_group, c[0])
            min_first_group = min(min_first_group, c[0])
        else:
            second_group.append(c)
            max_second_group = max(max_second_group, c[1])
            min_second_group = min(min_first_group, c[1])
    first_group = silly_sort(first_group, min_first_group, max_first_group, lambda c: c[0])
    second_group = reversed(list(silly_sort(second_group, min_second_group, max_second_group, lambda c: c[1])))

    order = chain(first_group, second_group)

    cum_sum = 0
    for c in order:
        cum_sum -= c[0]
        if cum_sum < 0:
            return 'No'
        cum_sum += c[1]
    if cum_sum == 0:
        return 'Yes'
    return 'No'

def __starting_point():
    main()

__starting_point()
