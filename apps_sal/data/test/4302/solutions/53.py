(a, b) = map(int, input().split())
if max(a, b) > min(a, b):
    print(2 * max(a, b) - 1)
else:
    print(2 * a)
