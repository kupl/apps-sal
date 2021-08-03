n = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
a, b = map(int, input().split())
a, b = n.index(a), n.index(b)
print(['DBroabw'[a < b::2], 'Alice'][a > b])
