import sys
sys.setrecursionlimit(10 ** 6)
(a, b) = map(int, input().split())


def calc(a):
    if a <= 0:
        return 0
    a += 1
    ans = 0
    for i in range(50):
        loop = 1 << i + 1
        cnt = a // loop * loop // 2
        cnt += max(0, a % loop - loop // 2)
        if cnt % 2 == 1:
            ans += 1 << i
    return ans


ans = calc(a - 1) ^ calc(b)
print(ans)
