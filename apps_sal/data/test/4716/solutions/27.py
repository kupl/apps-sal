_, k, *l = map(int, open(0).read().split())
l.sort(reverse=True)
print(sum(l[:k]))
