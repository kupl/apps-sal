import fractions


def solve(x, y):
    if fractions.gcd(x, y) > 1:
        return 'Impossible'
    turn = x > y
    if not turn:
        x, y = y, x
    ans = []
    while x != 0 and y != 0:
        ans.append((x // y, 'A' if turn else 'B'))
        x, y = y, x % y
        turn = not turn
    ans[-1] = (ans[-1][0] - 1, ans[-1][1])
    return ''.join(str(n) + l for n, l in ans)


x, y = [int(x) for x in input().split()]
print(solve(x, y))
