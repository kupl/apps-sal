N, A, B = map(int, input().split())
count = N // (A + B) * A
if N % (A + B) < A:
    count += N % (A + B)
else:
    count += A
print(count)
