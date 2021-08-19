from collections import Counter


def main():
    (n, k) = map(int, input().split())
    d = list(map(int, input().split()))
    counter = Counter()
    for x in d:
        counter[x % k] += 1
    ret = counter[0] // 2 * 2
    for i in range(1, k):
        if i != k - i:
            ret += min(counter[i], counter[k - i])
        else:
            ret += counter[i] // 2 * 2
    print(ret)


def __starting_point():
    main()


__starting_point()
