with open(0) as f:
    N, *a = map(int, f.read().split())
print(max(a)-min(a))
