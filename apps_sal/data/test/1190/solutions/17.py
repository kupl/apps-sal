w1, h1, w2, h2 = list(map(int, input().split()))

ans = 2 * (w1 + h1) + 2 * (w2 + h2) + 4

ans -= min(w1, w2) * 2

print(ans)
