from collections import defaultdict
n = input()
a = list(map(int, input().split()))


def solve(a):
    sum = a[0]
    res = 0
    size = 1
    counter = defaultdict(int)
    counter[a[0]] += 1
    for el in a[1:]:
        counter[el] += 1
        res = res - sum + size * el
        res = res - counter[el - 1] + counter[el + 1]
        size += 1
        sum += el
    return res


print(solve(a))
