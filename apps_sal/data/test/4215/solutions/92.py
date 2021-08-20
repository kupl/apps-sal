(a, b) = map(int, input().split())
uncovered = a - 2 * b
if uncovered > 0:
    print(uncovered)
else:
    print(0)
