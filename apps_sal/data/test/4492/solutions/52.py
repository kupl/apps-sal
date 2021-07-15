N, x = list(map(int, input().split()))
A = list(map(int, input().split()))

if x == 0:
    print((sum(A)))
    return

count = 0
for i in range(N - 1):
    d = A[i] + A[i + 1] - x
    if d <= 0:
        continue
    if A[i + 1] >= d:
        A[i + 1] -= d
        count += d
    else:
        count += d
        A[i] = d - A[i + 1]
        A[i + 1] = 0


print(count)

