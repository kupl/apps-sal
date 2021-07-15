import math

N = int(input())
S = int(input())

def f(B, N):
    X, res = N, 0
    while 0 < X:
        res += X % B
        X //= B
    return res


if N == S:
    print(N + 1)
    return

i = 2
while i * i <= N:
    if f(i, N) == S:
        print(i)
        return
    i += 1

sqrtN = math.floor(math.sqrt(N))
i = 1
ans = -1
while i * i < N:
    if (N - S) % i != 0:
        i += 1
        continue
    b = (N - S) // i + 1
    if sqrtN < b and f(b, N) == S:
        ans = b
    i += 1

print(-1 if ans == -1 else ans)
