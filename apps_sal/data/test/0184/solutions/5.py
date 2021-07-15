l, r, a = map(int, input().split())
print(l + r + a - max(abs(l - r) - a, 0) - (l + r + a - max(abs(l - r) - a, 0)) % 2)
