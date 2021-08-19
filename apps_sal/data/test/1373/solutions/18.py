(N, K) = list(map(int, input().split()))
x = 10
y = 10 + N
ans = 0
a = x
b = y
for i in range(1, N + 2):
    if i >= K:
        ans += b - a + 1
    a += x + i
    b += y - i
print(ans % (10 ** 9 + 7))
