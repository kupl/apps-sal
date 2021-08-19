from math import ceil


def main(n, k, a):
    a = set(a)
    n = len(a)
    if n > k == 1:
        return -1
    if n <= k:
        return 1
    return 1 + ceil((n - k) / (k - 1))


for i in range(int(input())):
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(main(n, k, a))
