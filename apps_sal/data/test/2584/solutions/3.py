import sys


def input():
    return sys.stdin.readline().strip()


T = int(input())


def solve(n, p, k, goods):
    i = 0
    ans = 0
    while i < n:
        if i < n - 1 and goods[i + 1] <= p:
            ans += 2
            p -= goods[i + 1]
            i += 2
        elif goods[i] <= p:
            ans += 1
            break
        else:
            i += 1
    return ans


for _ in range(T):
    (n, p, k) = list(map(int, input().split()))
    goods = list(map(int, input().split()))
    goods.sort()
    ans = solve(n, p, k, goods)
    if goods[0] <= p and n >= 2:
        ans = max(ans, solve(n - 1, p - goods[0], k, goods[1:]) + 1)
    print(ans)
