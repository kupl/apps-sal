n = int(input())
arr = [0]
sm = 0
smarr = 0
ten = 1
MOD = 998244353
for i in range(1, n + 1):
    ten = (ten * 10) % MOD
    all = i * ten % MOD
    sm = (sm + smarr) % MOD
    x = (all - sm + MOD) % MOD
    arr.append(x)
    smarr = (smarr + x) % MOD
    sm = (sm + x) % MOD
arr.reverse()
arr.pop()
print(*arr)
