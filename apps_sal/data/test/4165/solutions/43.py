(n, *l) = map(int, open(0).read().split())
l.sort(reverse=True)
print('Yes' if l[0] < sum(l[1:]) else 'No')
