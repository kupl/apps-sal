a, b = map(int, input().split())
if a == b:
    print(a * 2)
else:
    print(2 * max(a, b) - 1)
