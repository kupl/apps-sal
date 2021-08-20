(w1, h1, w2, h2) = map(int, input().split())
w = max(w1, w2)
h = h1 + h2
print(w + h + w + h + 4)
