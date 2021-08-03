a, b = map(int, input().split())
if 25 * (a + 1) <= 20 * b or 20 * (b + 1) <= 25 * a:
    print(-1)
else:
    print(max(10 * b, int((25 * a + 1) / 2)))
