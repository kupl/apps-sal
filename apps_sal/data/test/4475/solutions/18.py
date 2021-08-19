t = int(input())
for _ in range(t):
    (a, b, x, y, n) = map(int, input().split())
    mina1 = max(x, a - n)
    minb1 = max(y, b - (n - a + mina1))
    minb2 = max(y, b - n)
    mina2 = max(x, a - (n - b + minb2))
    print(min(mina1 * minb1, mina2 * minb2))
