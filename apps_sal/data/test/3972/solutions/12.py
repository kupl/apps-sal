P = 10 ** 9 + 7
N = int(input())
k = (N-1) ** 2 % P + 2
a, b, c = 1, 0, 0
ans = 0
for i in range(N-1):
    ans += a * (k + min(i, N-3))
    ans %= P
    a, b, c = a + b, b + c, a
    if a >= P: a -= P
    if b >= P: b -= P

ans += N * a
ans %= P
print(ans)
