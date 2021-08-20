import sys
sys.setrecursionlimit(100000)


def score(n):
    factor = 1
    ans = 0
    save = n
    while n > 0:
        ans += factor * (n & 1)
        n >>= 1
        factor *= 2
    return ans


def solve(n, r, half_size):
    if r == 0:
        return 0
    if n < 2:
        return n
    ans = 0
    if r > half_size:
        ans += n & 1
        ans += score(n // 2)
        ans += solve(n // 2, r - half_size - 1, half_size // 2)
    else:
        ans += solve(n // 2, r, half_size // 2)
    return ans


def main():
    (n, l, r) = list(map(int, input().split()))
    b = len(bin(n)) - 2
    half_size = (1 << b - 1) - 1
    right = solve(n, r, half_size)
    left = solve(n, l - 1, half_size)
    print(right - left)


main()
