a, b, c, d = map(int, input().split())

if a + b > c + d:
    ans = "Left"
elif a + b < c + d:
    ans = "Right"
else:
    ans = "Balanced"
print(ans)
