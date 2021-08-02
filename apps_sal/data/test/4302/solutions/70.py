a, b = list(map(int, input().split()))
if a != b:
    print((max(a, b) * 2 - 1))
else:
    print((a * 2))
