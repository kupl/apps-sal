(A, B) = list(map(int, input().split()))
max = -1 * 10 ** 10
if max < A + B:
    max = A + B
if max < A * B:
    max = A * B
if max < A - B:
    max = A - B
print(max)
