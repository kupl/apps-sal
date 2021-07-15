w, a, b = map(int, input().split())
l = max(a, b) - min(a, b)
print(l - w if l > w else 0)
