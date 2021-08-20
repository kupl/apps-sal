n = int(input())
p = 10 ** 9 + 7
ans = pow(10, n, mod=p) - 2 * pow(9, n, mod=p) + pow(8, n, mod=p)
print(ans % p)
