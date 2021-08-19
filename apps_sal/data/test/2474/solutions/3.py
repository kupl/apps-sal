n = int(input())
c = sorted(map(int, input().split()))
mod = 1000000007
ret = 0
for i in range(n):
    ret = (ret + (i + 2) * c[n - i - 1]) % mod
for i in range(n - 1):
    ret = ret * 4 % mod
print(ret)
