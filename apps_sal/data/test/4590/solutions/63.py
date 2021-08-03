N, M, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

b = 0
tb = 0

for i in range(M):
    if tb + B[i] > K:
        break
    tb += B[i]
    b = i + 1

ans = [0, b]
m = b
a = 0
ta = 0

for i in range(N):
    if ta + A[i] > K:
        break
    a = i + 1
    ta += A[i]
    while True:
        if ta + tb > K:
            if b == 0:
                break
            b -= 1
            tb -= B[b]
        else:
            if a + b > m:
                m = a + b
                ans = [a, b]
            break

print((ans[0] + ans[1]))
