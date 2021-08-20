(n, m) = list(map(int, input().split()))
K = [list(map(int, input().split()))[1:] for _ in range(m)]
p = list(map(int, input().split()))
ans = 0
for i in range(2 ** n):
    bit = [i >> j & 1 for j in range(n)]
    for (j, k) in enumerate(K):
        if p[j] != sum([bit[l - 1] for l in k]) % 2:
            break
    else:
        ans += 1
print(ans)
