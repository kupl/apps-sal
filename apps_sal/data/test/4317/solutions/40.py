a, b = map(int, input().split())
ans = max(a+b, a-b, a*b)
print(ans)
