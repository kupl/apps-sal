with open(0) as f:
    (N, K, *l) = map(int, f.read().split())
l.sort(reverse=True)
print(sum(l[:K]))
