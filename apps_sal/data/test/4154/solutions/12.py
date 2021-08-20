(n, m) = map(int, input().split())
(l_max, r_min) = (-1, float('inf'))
for i in range(m):
    (li, ri) = map(int, input().split())
    l_max = max(l_max, li)
    r_min = min(r_min, ri)
ans = r_min - l_max + 1 if r_min - l_max >= 0 else 0
print(ans)
