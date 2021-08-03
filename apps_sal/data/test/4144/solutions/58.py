n = int(input())
mod = 10**9 + 7
l = [8, 2, 0]
for i in range(n - 1):
    a, b, c = l
    l[0] = a * 8 % mod
    l[1] = (b * 9 + a * 2) % mod
    l[2] = (b + c * 10) % mod
print(l[2])
