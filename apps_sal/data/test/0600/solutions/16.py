(a, b) = (int(input()), int(input()))
(a, b) = (min(a, b), max(a, b))
m = (a + b) // 2
i = m - a
j = b - m
ans = (i + 1) * i // 2
ans += (j + 1) * j // 2
print(ans)
