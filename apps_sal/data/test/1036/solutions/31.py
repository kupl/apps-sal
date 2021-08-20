def merge(x, y):
    if x == y:
        return x
    if x != 'R' and y != 'R':
        return 'S'
    if x != 'P' and y != 'P':
        return 'R'
    return 'P'


def main():
    (n, k) = list(map(int, input().split()))
    S = input()
    cur = S
    for i in range(k):
        prev = cur
        cur = [None] * n
        for j in range(n):
            cur[j] = merge(prev[j * 2 % n], prev[(j * 2 + 1) % n])
    print(cur[0])


def __starting_point():
    main()


__starting_point()
