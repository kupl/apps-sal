n, a, b = list(map(int, input().split()))
mod = 1000000007
c = [1] * (b + 1)


def com(n, b):
    for i in range(1, b + 1):
        c[i] = c[i - 1] * ((n - i + 1) * pow(i, mod - 2, mod)) % mod


com(n, b)
ans = (pow(2, n, mod) - c[a] - c[b] - 1) % mod

print(ans)
