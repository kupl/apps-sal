t = int(input())
res = t
i = 2
while(i <= t):
    res = (res - 1) * i % 998244353
    i += 1
print(res)
