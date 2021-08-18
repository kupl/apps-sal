
N, = map(int, input().split())
A = list(map(int, input().split()))
c = 0
n = len(A)
if len(A) < 3:
    print(0)
    return
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if (2 * max(A[i], A[j], A[k]) - sum([A[i], A[j], A[k]]) >= 0) or A[i] == A[j] or A[j] == A[k] or A[k] == A[i]:
                continue
            c += 1
print(c)
