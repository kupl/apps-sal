n, d = list(map(int, input().split()))
x = list(map(int, input().split()))

print(min(len([yi for yi in x if yi < xi or xi + d < yi]) for xi in x))

