A, B = map(int, input().split())

start = A + B
if start < 24:
    print(start)
else:
    start = start - 24
    print(start)
