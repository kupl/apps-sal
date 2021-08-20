(a, b) = map(int, input().split())
if a != b:
    button = max(a, b)
    all = 0
    all += button * 2 - 1
    print(all)
else:
    print(a * 2)
