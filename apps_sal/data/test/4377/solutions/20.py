n = [int(x) for x in input().split()]
m = max(n)
n.remove(m)
print(' '.join((str(m - x) for x in n)))
