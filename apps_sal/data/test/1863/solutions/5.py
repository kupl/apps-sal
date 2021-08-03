"""http://codeforces.com/problemset/problem/282/B"""

from sys import stdin
_data = iter(stdin.read().split('\n'))
def input(): return next(_data)


def __starting_point():
    n = int(input())
    ans = ''
    sum_a = sum_g = 0
    for _ in range(n):
        a, g = list(map(int, input().split()))
        if sum_a + a <= sum_g + 500:
            ans += 'A'
            sum_a += a
        else:
            ans += 'G'
            sum_g += g
    print(ans)


__starting_point()
