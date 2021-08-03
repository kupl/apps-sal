n = int(input())
A = list(map(int, input().split()))
w = 1
res = 0
f = 0
for q in range(0, n - 1):
    if f != 0 and A[q + 1] - A[q] != res:
        w = 0
        break
    elif f == 0:
        res = A[q + 1] - A[q]
        f = 1
if w == 0:
    print(A[len(A) - 1])
else:
    print(A[len(A) - 1] + res)
