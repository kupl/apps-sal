(n, a, b) = map(int, input().split())
(div, mod) = divmod(n, a + b)
ans = div * a + min(mod, a)
print(ans)
