n = int(input())
p = list(map(int, input().split()))
id = [0] * (n + 1)
for (i, p_i) in enumerate(p):
    id[p_i] = i
r = list(range(1, n + 1)) + [n, n]
l = list(range(-1, n - 1)) + [-1, -1]
ans = 0
for p in range(1, n + 1):
    x = id[p]
    r1 = r[x]
    r2 = r[r1]
    l1 = l[x]
    l2 = l[l1]
    ans += p * ((x - l1) * (r2 - r1) + (l1 - l2) * (r1 - x))
    r[l1] = r1
    l[r1] = l1
print(ans)
