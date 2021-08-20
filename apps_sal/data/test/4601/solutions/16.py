(n, k) = map(int, input().split())
h = sorted(map(int, input().split()))
print(sum(h[:-k]) if k != 0 else sum(h))
