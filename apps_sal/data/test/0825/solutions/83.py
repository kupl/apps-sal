import math


def solve():
    N = int(input())
    ans = 0
    for i in range(2, int(math.sqrt(N)) + 2):
        n = 1
        cnt = 0
        while N % i == 0:
            N //= i
            cnt += 1
            if cnt == n:
                cnt = 0
                n += 1
                ans += 1
    if N != 1:
        ans += 1
    return ans


print(solve())
