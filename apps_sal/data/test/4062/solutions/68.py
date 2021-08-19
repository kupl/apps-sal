(a, b, c, d) = map(int, input().split())
ans = []
ans.append(a * c)
ans.append(a * d)
ans.append(b * c)
ans.append(b * d)
print(max(ans))
