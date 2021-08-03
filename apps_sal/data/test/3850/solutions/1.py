def o(): return [int(f)for f in input().split()]


n, k, p = o()
a = sorted(o())
b = sorted(o())
print(min(max(abs(b[i + d] - a[i]) + abs(b[i + d] - p) for i in range(n)) for d in range(k - n + 1)))
