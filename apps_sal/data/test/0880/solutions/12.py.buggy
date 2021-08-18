n = int(input())
dd = 998244353
dp = [(1, 0), (1, 0), (2, 0), (6, 3)]
if n == 1:
    print(1)
    return
elif n == 2:
    print(2)
    return

for i in range(4, n + 1):
    np = (dp[-1][0] * i, i * (dp[-1][0] - 1) + i * (dp[-1][1]))
    np = (np[0] % dd, np[1] % dd)
    dp.append(np)

print((dp[-1][0] + dp[-1][1]) % dd)
