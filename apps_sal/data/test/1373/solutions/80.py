from math import factorial
n, k = [int(i) for i in input().split()]
mod = 10 ** 9 + 7

def s(n, m=0): # m~nの総和
    nonlocal mod
    return (n * (n+1) // 2 - (n-m) * (n-m+1) // 2) % mod

sm = 0
for i in range(k, n+1):
    sm = (sm + s(n, i) - s(i-1, i-1) + 1) % mod

print((sm+1) % mod)
