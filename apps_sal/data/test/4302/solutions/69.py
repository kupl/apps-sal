a, b = list(map(int, input().split()))
if a == b:
    print((a+b))
else:
    print((max(a, b) + max(a, b) -1))

