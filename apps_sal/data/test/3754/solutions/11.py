import sys
readline = sys.stdin.readline
read = sys.stdin.read
n = int(readline())
(*d,) = map(int, readline().split())
MOD = 998244353
ans = 1
v = sum(d) - n
for i in range(n - 2):
    ans *= v
    ans %= MOD
    v -= 1
for i in d:
    ans *= i
    ans %= MOD
print(ans)
