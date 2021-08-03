n, k = map(int, input().split())
h = list(map(int, input().split()))
print(sum(sorted(h)[:n - k]) if n - k > 0 else 0)
