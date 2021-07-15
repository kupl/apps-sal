d1, d2, d3 = map(int, input().split())
ans = min(d1+d2+d3, 2 * d1 + 2 * d3, 2 * d2 + 2 * d3, 2 * d1 + 2 * d2)
print(ans)
