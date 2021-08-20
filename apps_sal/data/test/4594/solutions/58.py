with open(0) as f:
    (N, *d) = list(map(int, f.read().split()))
d = list(set(d))
print(len(d))
