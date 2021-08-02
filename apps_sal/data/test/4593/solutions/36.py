X = int(input())
ans = 1
for i in range(2, int(X**0.5) + 1):
    x = i
    while x <= X:
        ans = max(ans, x)
        x *= i
print(ans)
