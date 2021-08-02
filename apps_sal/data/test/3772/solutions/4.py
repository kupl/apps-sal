a, b = [int(x) for x in input().split()]
ans = 0
while (a != 1 and b != 1):
    if (a > b):
        ans += a // b
        a %= b
    a, b = b, a
ans += a + b - 1
print(ans)
