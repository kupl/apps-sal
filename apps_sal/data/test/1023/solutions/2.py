from bisect import bisect_left

(n, m, ta, tb, k) = (int(x) for x in input().split())
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]

# ans = b[-1] + tb # last flight
ans = 0

if len(a) <= k or len(b) <= k:
    print(-1)
    return

for i in range(k + 1):
    v = bisect_left(b, a[i] + ta)
    if v + (k - i) < len(b):
        ans = max(ans, b[v + (k - i)] + tb)
    else:
        print(-1)
        return

print(ans)

