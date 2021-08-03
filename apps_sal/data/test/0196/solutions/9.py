x, k = map(int, input().split())
mod = 1000000007
flag = True
if x == 0:
    flag = False

x = x % mod
y = pow(2, k + 1, mod)
z = pow(2, k, mod) - 1

x = x * y
x = x % mod
x = x - z
if x == 0:
    x = x + mod
x = x % mod

if flag:
    print(x)
else:
    print(0)
