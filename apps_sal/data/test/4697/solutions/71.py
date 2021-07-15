s, c = map(int, input().split())
print((s + (c - s * 2) // 4, c // 2)[s * 2 >= c])
