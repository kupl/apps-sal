a, b, c = map(int, input().split())
print('YNEOS'[b - a != c - b::2])
