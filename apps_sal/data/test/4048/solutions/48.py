n = int(input())
ans = 10 ** 12
for i in range(int(n ** 0.5) + 1):
    a = i + 1
    if n % a == 0:
        b = n // a
        ans = min(ans, a + b - 2)
print(ans)
