a, b, c = list(map(int, input().split()))

ans = a + b

ans = min(ans, min(a, b) + c)

ans *= 2

ans = min(ans, a + b + c)
print(ans)
