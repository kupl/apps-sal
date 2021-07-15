n, a, b = map(int, input().split())
t = [w - 1 - (((w * a) // b) * b - 1) // a for w in map(int, input().split())]
print(' '.join(map(str, t)))
