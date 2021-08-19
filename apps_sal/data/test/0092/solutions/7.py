from fractions import gcd
(a, b, c) = list(map(int, input().split()))
ans = 0
mod = 1073741824
div = [0] * 1000001
for i in range(1, 1000001):
    j = i
    while j <= 1000000:
        div[j] += 1
        j += i
for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            ans += div[i * j * k]
print(ans % mod)
