(x, y) = map(int, input().split())


def count(x, y):
    ans = 0
    while x <= y:
        x *= 2
        ans += 1
    return ans


print(count(x, y))
