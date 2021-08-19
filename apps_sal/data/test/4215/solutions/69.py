(A, B) = map(int, input().split())
if 2 * B >= A:
    print(0)
else:
    print(A - 2 * B)
