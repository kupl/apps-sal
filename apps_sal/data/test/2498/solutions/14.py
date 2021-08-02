def GCM(x, y):
    if x % y == 0:
        return y
    else:
        return GCM(y, x % y)


N, M = map(int, input().split())

A = list(map(int, input().split()))

count2 = [0 for i in range(N)]
for i in range(N):
    a = A[i]
    while a % 2 == 0:
        count2[i] += 1
        a = a // 2
    A[i] = a
if sum(count2) == count2[0] * N:
    count2 = count2[0]
    buf = 1
    for i in range(N):
        buf = A[i] * buf // GCM(buf, A[i])
    buf *= 2**(count2 - 1)
    # print(buf)
    n = M // buf
    print((n + 1) // 2)

else:
    print(0)
