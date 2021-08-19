def solve(n):
    res = 0
    for x in range(n + 1):
        if n ^ x == n - x:
            res += 1
    return res


def solve_1(n):
    cnt = 0
    while n:
        if n % 2 == 1:
            cnt += 1
        n = n // 2
    return 2 ** cnt


t = int(input())
while t:
    n = int(input())
    print(solve_1(n))
    t -= 1
