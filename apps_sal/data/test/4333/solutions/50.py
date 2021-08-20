(a, b, c, d) = map(int, input().split())
x = c - a
y = d - b
ans1 = a + x - y
ans2 = b + x + y
ans3 = a - y
ans4 = b + x
print(ans1, ans2, ans3, ans4)
