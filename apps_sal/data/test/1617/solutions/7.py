from math import sqrt
n = int(input())
ans = []
for p in range(1, n + 1):
    ps = p ** 2
    if ps > n:
        break
    if n % p == p % p:
        ans.append(p * (n + 2 - n // p) // 2)
        if ps < n:
            ans.append(n // p * (n + 2 - p) // 2)
ans.sort()
print(*ans)
