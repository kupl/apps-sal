(x, y) = list(map(str, input().split()))
l = ['A', 'B', 'C', 'D', 'E', 'F']
print(['=', '<', '>'][l.index(y) > l.index(x) or -(l.index(y) < l.index(x))])
