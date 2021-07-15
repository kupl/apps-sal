N = int(3e5+3)
MOD = int(1e9+7)
pow2 = [1] * N
for i in range(1, N):
    pow2[i] = pow2[i-1] * 2 % MOD

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

def add(x, y):
    return ((x % MOD + MOD) + (y % MOD + MOD) + MOD) % MOD
def substract(x, y):
    return ((x % MOD + MOD) - (y % MOD + MOD) + MOD) % MOD
def multiple(x, y):
    return ((x % MOD) * (y % MOD)) % MOD

res = 0
for i in range(1, n):
    diff = arr[i] - arr[i-1]
    cnt = multiple(substract(pow2[i], 1), substract(pow2[n-i], 1))
    res = add(res, multiple(cnt, diff))
print(res)

