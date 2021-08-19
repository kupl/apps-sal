(A, B) = map(int, input().split())
start = A + B
if start >= 24:
    print(start - 24)
else:
    print(start)
