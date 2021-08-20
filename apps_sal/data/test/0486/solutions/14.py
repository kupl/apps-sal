def calc(n):
    ret = 1
    while n != 0:
        ret *= n % 10
        n //= 10
    return ret


def solve():
    n = int(input())
    ans = calc(n)
    for i in range(1, 10):
        a = (n + 1) % 10 ** i
        if n < a:
            break
        ans = max(ans, calc(n - a))
    return ans


print(solve())
