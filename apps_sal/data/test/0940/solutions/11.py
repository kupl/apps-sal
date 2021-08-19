(a, b, c) = list(map(int, input().split()))
(a, b, c) = (min(a, b, c), sum([a, b, c]) - max(a, b, c) - min(a, b, c), max(a, b, c))
print(max(0, c - a - b + 1))
