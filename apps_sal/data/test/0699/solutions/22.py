(y, k, n) = list(map(int, input().split()))
A = n // k * [0]
pos = 0
for i in range(1, n // k + 1):
    x = i * k - y
    if 1 <= x:
        A[pos] = x
        pos += 1
if pos == 0:
    print(-1)
else:
    print(' '.join(map(str, A[:pos])))
