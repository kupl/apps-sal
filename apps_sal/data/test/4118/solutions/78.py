(a, b) = map(int, input().split())
if max(a, b) <= 9:
    print(a * b)
else:
    print(-1)
