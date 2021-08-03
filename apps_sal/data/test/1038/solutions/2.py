import sys
input = sys.stdin.readline

A, B = map(int, input().split())


def xor_sum(n):
    ans = 0
    if n % 2:
        ans = ((n + 1) // 2) % 2
    else:
        ans = (n // 2) % 2
        ans ^= n
    return ans


print(xor_sum(A - 1) ^ xor_sum(B))
