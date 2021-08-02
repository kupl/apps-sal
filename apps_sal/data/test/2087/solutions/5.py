r = 1
for n in list(map(int, input().split())):
    s = n * (n + 1) // 2 % 998244353
    r = r * s % 998244353
print(int(r))
