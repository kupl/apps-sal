Q = int(input())


def solve():
    [c, m, x] = list(map(int, input().split()))

    def canMakeK(k):
        if c < k or m < k:
            return False
        return ((c - k) + (m - k) + x) >= k

    ans = 0
    jump = max(c, m, x)
    while jump > 0:
        while canMakeK(ans + jump):
            ans += jump
        jump //= 2

    return ans


for _ in range(Q):
    print(solve())
