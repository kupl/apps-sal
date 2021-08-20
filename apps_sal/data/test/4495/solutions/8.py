(a, b, x) = map(int, input().split())
c = b - a + a % x
if a % x != 0:
    print(c // x)
else:
    print(c // x + 1)
