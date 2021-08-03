import bisect
N, M, *AB = [int(_) for _ in open(0).read().split()]
AB = sorted(zip(AB[::2], AB[1::2]))
l, r = AB[0]
ans = 1
for a, b in AB[1:]:
    if r <= a:
        l, r = a, b
        ans += 1
    else:
        r = min(r, b)
print(ans)
