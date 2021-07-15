a, b = map(int, input().split())

if a > b or a < b:
    m = max(a, b)
    print(2 * m - 1)
elif a == b:
    print(a + b)
