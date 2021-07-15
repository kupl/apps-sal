n, w = map(int, input().split())
a = sorted(map(int, input().split()))
print(3 * n * min(w / 3 / n, a[0], a[n] / 2))
