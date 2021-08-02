# n = int(input())
# w, h = map(int, input().split())
# to_zero_based = lambda x: int(x) - 1
from fractions import gcd


def main():
    n, x, y = list(map(int, input().split()))
    monsters = [int(input()) for _ in range(n)]

    if x == y:
        results = ['Both'] * n
    else:
        results = []
        g = gcd(x, y)
        x //= g
        y //= g
        turns = [i * x for i in range(1, y)] + [i * y for i in range(1, x)]
        turns.sort()
        freq_sum = x + y
        for monster in monsters:
            monster %= freq_sum
            if monster == 0 or monster == freq_sum - 1:
                results.append('Both')
            else:
                results.append('Vanya' if turns[monster - 1] % y == 0 else 'Vova')

    print('\n'.join(results))


main()
