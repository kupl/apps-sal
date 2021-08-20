(n, m) = map(int, input().split())
l = [0 for i in range(m)]
for i in range(n):
    ka = [int(x) for x in input().split()]
    k = ka[0]
    for j in range(1, k + 1):
        l[ka[j] - 1] += 1
ans = 0
for i in l:
    if i == n:
        ans += 1
print(ans)
