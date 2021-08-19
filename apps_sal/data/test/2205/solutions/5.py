from functools import reduce


def R():
    return map(int, input().split())


n = int(input())
a = R()
ans = reduce(lambda x, y: x ^ y, a)
f = [0]
for i in range(1, n + 1):
    f.append(f[-1] ^ i)
for i in range(1, n + 1):
    if n // i % 2:
        ans ^= f[i - 1]
    ans ^= f[n % i]
print(ans)
