from collections import Counter


def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    counter = Counter(A)
    n_odd, n_even = 0, 0
    for c in counter.values():
        if c % 2 == 0:
            n_even += 1
        else:
            n_odd += 1
    print(n_odd + (n_even // 2) * 2)


def __starting_point():
    main()
__starting_point()
