w1, h1, w2, h2 = list(map(int, input().split()))

ans = 0
ans += (w1 + 1) * 2 + (h1 * 2)
ans += (w2 + 1) * 2 + (h2 * 2)
ans -= 2 * (min(w2, w1))
print(ans)
