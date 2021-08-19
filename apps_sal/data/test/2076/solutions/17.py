def f1(a, b, c):
    res = 0
    d = min(b, c // 2)
    res += 3 * d
    b -= d
    res += min(a, b // 2) * 3
    return res


def f2(a, b, c):
    res = 0
    d = min(a, b // 2)
    res += 3 * d
    b -= 2 * d
    res += min(b, c // 2) * 3
    return res


t = int(input())
for i in range(t):
    (a, b, c) = list(map(int, input().split()))
    print(max(f1(a, b, c), f2(a, b, c)))
