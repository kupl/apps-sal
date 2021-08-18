
from collections import Counter


def main():
    n = int(input())
    t = list(map(int, input().split()))

    counter = Counter()
    counter[t[0]] = 1

    ret = 0
    for i in range(1, n):
        if t[i] == t[i - 1]:
            counter[t[i]] += 1
        else:
            counter[t[i]] = 1
        ret = max(ret, min(counter[1], counter[2]) * 2)
    print(ret)


def __starting_point():
    main()


__starting_point()
