__author__ = 'nobik'


def count(a, b, c, x):
    if a < b + c:
        return 0
    value = min(x, a - b - c)
    return (value + 1) * (value + 2) // 2


(a, b, c, l) = list(map(int, input().split()))
ans = (l + 1) * (l + 2) * (l + 3) // 6
for i in range(l + 1):
    ans -= count(a + i, b, c, l - i)
    ans -= count(b + i, a, c, l - i)
    ans -= count(c + i, a, b, l - i)
print(ans)
