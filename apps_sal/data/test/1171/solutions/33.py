(n, k) = list(map(int, input().split()))
v = [int(i) for i in input().split()]
ans = 0
for a in range(min(n, k) + 1):
    (pa, va) = (v[:a], v[a:])
    for b in range(min(n, k) - a + 1):
        pb = pa + va[-b:] if b > 0 else pa
        pb.sort()
        s = sum(pb)
        ans = max(s, ans)
        for c in range(min(k - a - b, a + b)):
            s -= pb[c]
            ans = max(s, ans)
print(ans)
