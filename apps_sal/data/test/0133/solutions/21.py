n, m = list(map(int, input().split()))

MOD = 10**9 + 7

p1 = pow(2, m, MOD) - 1
p2 = pow(p1, n, MOD)

print(p2)
