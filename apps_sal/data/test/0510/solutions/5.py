(*l, d) = map(int, input().split())
l.sort()
print(max(d - (l[1] - l[0]), 0) + max(d - (l[2] - l[1]), 0))
