n = int(input())
r = 0
i = 2
while i * 2 <= n:
    a = int(n / i)
    r += (a + 2) * (a - 2 + 1) / 2
    i += 1
print(int(4 * r))
