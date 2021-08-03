N = int(input())
*A, = sorted(map(int, input().split()), reverse=True)

n = N - 2
a = A[0]
i = 1
while 0 < n:
    if n == 1:
        a += A[i]
        break
    a += A[i] * 2
    i += 1
    n -= 2
print(a)
