(_, *l) = map(int, open(0).read().split())
c = len(set(l))
print(c - 1 + c % 2)
