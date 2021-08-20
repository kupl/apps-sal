def read():
    return list(map(int, input().split()))


def vect(a, b):
    return a[0] * b[1] - a[1] * b[0]


def vector(A, B):
    return (B[0] - A[0], B[1] - A[1])


n = int(input())
p = [tuple(read()) for i in range(n)]
cnt = 0
for i in range(2, n):
    v1 = vector(p[i], p[i - 1])
    v2 = vector(p[i - 1], p[i - 2])
    if vect(v1, v2) < 0:
        cnt += 1
print(cnt)
