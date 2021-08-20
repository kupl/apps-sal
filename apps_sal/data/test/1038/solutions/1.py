import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
(a, b) = list(map(int, input().split()))


def xor_sum(n):
    ans = 0
    if n % 2:
        ans = (n + 1) // 2 % 2
    else:
        ans = n // 2 % 2
        ans ^= n
    return ans


print(xor_sum(b) ^ xor_sum(a - 1))
