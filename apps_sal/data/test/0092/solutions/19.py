(a, b, c) = [int(x) for x in input().split(' ')]
mod = 1073741824
divisors = [1] * 1000001
for x in range(2, 1000001):
    for y in range(x, 1000001, x):
        divisors[y] += 1
ans = 0
for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            ans += divisors[i * j * k] % mod
print(ans % mod)
