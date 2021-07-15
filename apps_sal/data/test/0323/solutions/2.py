read = lambda: map(int, input().split())
a, b = read()
x = min(a, b)
ans = 1
for i in range(2, x + 1):
    ans *= i
print(ans)
