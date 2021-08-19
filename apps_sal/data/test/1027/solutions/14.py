n = 14
a = [int(v) for v in input().split()]
assert len(a) == n
ans = 0
for i in range(n):
    if a[i] == 0:
        continue
    (q, r) = divmod(a[i], n)
    curr = 0
    for j in range(n):
        val = (a[(i + j) % n] if j != 0 else 0) + q + (1 if 1 <= j <= r else 0)
        if val % 2 == 0:
            curr += val
    ans = max(ans, curr)
print(ans)
