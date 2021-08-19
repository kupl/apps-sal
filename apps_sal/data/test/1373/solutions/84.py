n, k = list(map(int, input().split()))

MOD = (10 ** 9) + 7
ans = 0

min_val = 0
max_val = n
p = 1

for i in range(n + 1):
    # print(min_val, max_val)
    if i + 1 >= k:
        ans += max_val - min_val + 1
        ans = ans % MOD
    min_val += p
    max_val += n - p
    p += 1

print(ans)
