n, k = map(int, input().split())
mod = 10**9 + 7

sm = 0
for i in range(k, n + 2):
    sm += n * (n + 1) // 2
    sm -= (n - i) * (n - i + 1) // 2
    sm -= (i - 1) * i // 2
    sm += 1
    sm %= mod

print(sm)
