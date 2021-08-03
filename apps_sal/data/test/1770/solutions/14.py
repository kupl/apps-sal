def get(x, y, d):
    if abs(x - y) % d == 0:
        return abs(x - y) // d
    return -1


def moves(x, y, d):
    return (abs(x - y) + d - 1) // d


T = int(input())
for _ in range(T):
    (n, x, y, d) = list(map(int, input().split(' ')))
    ans = int(2e9)
    if abs(x - y) % d == 0:
        ans = abs(x - y) // d
    else:
        if get(1, y, d) != -1:
            ans = min(ans, moves(x, 1, d) + get(1, y, d))
        if get(n, y, d) != -1:
            ans = min(ans, moves(x, n, d) + get(n, y, d))
    print(ans if ans != int(2e9) else -1)
