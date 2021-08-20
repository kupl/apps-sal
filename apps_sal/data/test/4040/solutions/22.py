import sys
input = sys.stdin.readline


def main():
    (n, m, d) = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    current = -1
    ans = [0] * (1000 * 1000)
    for (i, c) in enumerate(C):
        current += d - 1
        for j in range(c):
            current += 1
            ans[current] = i + 1
    if current + d < n:
        print('NO')
    else:
        print('YES')
        amari = current - (n - 1)
        count = 0
        for a in ans:
            if a == 0 and amari > 0:
                amari -= 1
                continue
            count += 1
            print(a, end=' ')
            if count == n:
                break
        print('')


def __starting_point():
    main()


__starting_point()
