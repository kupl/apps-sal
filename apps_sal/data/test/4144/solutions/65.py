n = int(input())
m = 10 ** 9 + 7
u = pow(10, n, m)
a = (u - pow(9, n, m)) % m
b = (u - pow(8, n, m)) % m
ans = (a + a - b) % m
print(ans)
