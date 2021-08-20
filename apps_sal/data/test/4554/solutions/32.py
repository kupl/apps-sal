(w, a, b) = map(int, input().split())
ans = max(a, b) - min(a + w, b + w)
print(max(ans, 0))
