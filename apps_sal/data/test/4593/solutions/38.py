X = int(input())
ans = 1
for i in range(2, X + 1):
    t = i * i
    while t <= X:
        ans = max(ans, t)
        t *= i
print(ans)
