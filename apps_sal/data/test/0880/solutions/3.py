n = int(input())
fac = 1
for i in range(2, n + 1):
    fac = fac * i % 998244353
total = (n - 1) * fac % 998244353
dsum = 0
diff = 1
for i in range(0, n - 2):
    diff = diff * (n - i) % 998244353
    dsum += diff % 998244353
answer = (total - dsum) % 998244353
if n == 1:
    print(1)
else:
    print(answer)
