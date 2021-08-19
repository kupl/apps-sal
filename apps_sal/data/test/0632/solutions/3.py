"""input
3
5 1
8 2
3 4
"""


def solve():
    (n, k) = map(int, input().split())
    div = 0
    for i in range(2, n + 1):
        if n % i == 0:
            div = i
            break
    print(n + div + (k - 1) * 2)
    return


t = 1
t = int(input())
while t > 0:
    t -= 1
    solve()
