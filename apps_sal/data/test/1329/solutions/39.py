from itertools import permutations
# 3*5*5
# (2, 4, 4) (14, 4) (2, 24) (74)
n = int(input())
d = [0] * (n + 1)
for i in range(2, n + 1):
    for p in range(2, n + 1):
        while i % p == 0:
            i //= p
            d[p] += 1
d = list(filter(int, d))
ans = 0
for i, j, k in permutations(d, 3):
    ans += min(i - 2, j - 4, k - 4) >= 0
ans //= 2
for i, j in permutations(d, 2):
    ans += min(i - 14, j - 4) >= 0
    ans += min(i - 2, j - 24) >= 0
for i in d:
    ans += i - 74 >= 0
print(ans)
