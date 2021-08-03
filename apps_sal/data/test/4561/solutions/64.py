x, a, b = map(int, input().split())
print([["delicious", "safe"][a < b], "dangerous"][x + a < b])
