(p, q, r) = map(int, input().split())
ans = p + q + r - max(p, q, r)
print(ans)
