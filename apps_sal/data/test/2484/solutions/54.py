import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    res = 0
    left = 0
    add_total = 0
    xor_total = 0
    for right in range(n):
        add_total += A[right]
        xor_total ^= A[right]
        while add_total != xor_total:
            add_total -= A[left]
            xor_total ^= A[left]
            left += 1
        res += right - left + 1
    print(res)


def __starting_point():
    resolve()


__starting_point()
