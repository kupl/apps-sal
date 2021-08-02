mod = 1000000007
x, y = map(int, input().split())
n = int(input())
A = [x - y, x, y, y - x, -x, -y]
n %= 6
print((A[n] % mod + mod) % mod)
