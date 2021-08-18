3


def solve(a, l):
    if l == 0:
        return 0

    if l == 1:
        return a[0]

    k = 0
    while (2 ** k) < l:
        k += 1

    return min(a[k], a[k - 1] + solve(a, l - (2 ** (k - 1))))


def main():
    n, l = list(map(int, input().split()))
    a = list(map(int, input().split()))

    for i in range(n - 2, -1, -1):
        if a[i] > a[i + 1]:
            a[i] = a[i + 1]

    for i in range(1, n):
        if a[i] > 2 * a[i - 1]:
            a[i] = 2 * a[i - 1]

    while len(a) < 35:
        a.append(2 * a[len(a) - 1])

    print(solve(a, l))


main()
