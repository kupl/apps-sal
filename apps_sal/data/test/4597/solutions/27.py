n = int(input())
x = 1
for i in range(n):
    x *= (n - i)
    if x > 10**9 + 7:
        y = x // (10**9 + 7)
        x -= y * (10**9 + 7)

print(x)
