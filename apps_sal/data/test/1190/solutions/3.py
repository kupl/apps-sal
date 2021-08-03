w1, h1, w2, h2 = map(int, input().split())

ans = w1 + 2 + w2 + 2 + h1 + h2 + h1 + h2 + abs(w2 - w1)
print(ans)
