(a, b) = map(int, input().split())
height = (b - a) * (b - a + 1) // 2
ans = height - b
print(ans)
