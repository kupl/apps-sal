def main():
    from math import gcd
    import sys
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    max_a = 10 ** 6
    numbers = [0 for _ in range(max_a + 1)]
    for ai in a:
        numbers[ai] += 1
    is_pairwise = True
    for i in range(2, max_a + 1):
        count = 0
        for j in range(i, max_a + 1, i):
            count += numbers[j]
            if count > 1:
                is_pairwise = False
    if is_pairwise:
        print('pairwise coprime')
        return
    value_gcd = 0
    for i in range(n):
        value_gcd = gcd(value_gcd, a[i])
        if value_gcd == 1:
            print('setwise coprime')
            return
    print('not coprime')


def __starting_point():
    main()


__starting_point()
