def in_bounds(x, n):
    return 0 <= x < n


(n, a) = list(map(int, input().split()))
t = list(map(int, input().split()))
a -= 1
ans = t[a]
for d in range(1, n):
    l = a - d
    r = a + d
    if in_bounds(l, n) and in_bounds(r, n) and (t[l] == 1) and (t[r] == 1):
        ans += 2
    elif not in_bounds(l, n) and in_bounds(r, n) and (t[r] == 1):
        ans += 1
    elif in_bounds(l, n) and (not in_bounds(r, n)) and (t[l] == 1):
        ans += 1
print(ans)
