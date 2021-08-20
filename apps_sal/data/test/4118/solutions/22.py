(a, b) = map(int, input().split())
if a < 1 or a > 9 or b < 1 or (b > 9):
    print(-1)
else:
    print(a * b)
