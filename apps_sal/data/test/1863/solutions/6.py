"""http://codeforces.com/problemset/problem/282/B"""
from sys import stdin


def __starting_point():
    n = int(stdin.readline())
    ans = ''
    sum_a = sum_g = 0
    for _ in range(n):
        (a, g) = list(map(int, stdin.readline().split()))
        if sum_a + a <= sum_g + 500:
            ans += 'A'
            sum_a += a
        else:
            ans += 'G'
            sum_g += g
    print(ans)


__starting_point()
