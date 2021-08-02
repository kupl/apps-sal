n, k = map(int, input().split())
s = 0
for i in range(1, n + 1):
    q, r = divmod(n + 1, i)
    s += q * max(i - k, 0) + max(r - k, 0)
s -= n * (k == 0)
print(s)
