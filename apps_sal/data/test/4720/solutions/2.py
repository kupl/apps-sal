with open(0) as f:
    N, *lr = map(int, f.read().split())
print(sum(lr[1::2])-sum(lr[::2])+N)
