from collections import Counter


def go(a, b, counter):
    res, c = 0, a + b
    if counter.get(c) and counter[c] > 0:
        counter[c] -= 1
        res = max(res, go(b, c, counter) + 1)
        counter[c] += 1
    return res


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    counter = Counter(a)
    res = 2
    for a in counter:
        for b in counter:
            if (a != 0 or b != 0) and (a != b or counter[a] > 1):
                counter[a] -= 1
                counter[b] -= 1
                res = max(res, go(a, b, counter) + 2)
                counter[a] += 1
                counter[b] += 1
    res = max(res, counter[0])
    print(res)


main()
