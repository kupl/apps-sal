(n, m, z) = [int(el) for el in input().split()]
ans = 0
for i in range(1, z + 1):
    if i % n == i % m == 0:
        ans += 1
print(ans)
