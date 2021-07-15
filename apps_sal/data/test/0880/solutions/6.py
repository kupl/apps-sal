n = int(input())
last = n - 1
for i in range(3, n + 2):
    last = (last * (i - 1) - 1) % 998244353
print(last + 1)
