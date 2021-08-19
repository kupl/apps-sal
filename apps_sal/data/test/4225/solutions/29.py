(a, b, c, x) = map(int, input().split())
ans = 0
ans += min(a, x)
x -= min(a, x)
x -= min(b, x)
ans -= min(c, x)
x -= min(c, x)
print(ans)
