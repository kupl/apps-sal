3


def transform(a, b, c, y):
    ans = 0
    while True:
        if a == b == c == y:
            return ans
        (a, b, c) = sorted([a, b, c], reverse=True)
        c = min(a + b - 1, y)
        ans += 1


(x, y) = list(map(int, input().split()))
print(transform(y, y, y, x))
