(n, a) = list(map(int, input().split()))
c = list(map(int, input().split()))
res = c[a - 1]
for i in range(1, max(n - a + 1, a)):
    (l, r) = (a - 1 - i, a - 1 + i)
    if l >= 0 and r < n:
        if c[l] and c[r]:
            res += 2
    elif l >= 0:
        if c[l]:
            res += 1
    elif r < n:
        if c[r]:
            res += 1
print(res)
