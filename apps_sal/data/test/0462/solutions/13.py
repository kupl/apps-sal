a, b, c = [int(x) for x in input().split()]

print(min(abs(a - b) + abs(a - c), abs(a - c) + abs(b - c), abs(a - b) + abs(c - b)))
