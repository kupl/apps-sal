N, K = [int(_) for _ in input().split()]

s = 0
e = 0
ans = 0

MOD = 10 ** 9 + 7

for i in range(N+1):
    s += i 
    e += N - i 
    if i + 1 >= K:
        ans += e - s + 1
        ans %= MOD
print(ans)

