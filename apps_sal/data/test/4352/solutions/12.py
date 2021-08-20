(a, b) = list(map(int, input().split()))
l = [i for i in range(2, 14)] + [1]
print(['Draw', 'Alice', 'Bob'][l.index(a) > l.index(b) or -(l.index(a) < l.index(b))])
