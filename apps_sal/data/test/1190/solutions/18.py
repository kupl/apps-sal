(w1, h1, w2, h2) = map(int, input().split())
p = w1 + 2
p += h1 * 2
p += w1 - w2
p += h2 * 2
p += w2 + 2
print(p)
