import sys
def Ii(): return int(sys.stdin.readline())
def Mi(): return map(int, sys.stdin.readline().split())
def Li(): return list(map(int, sys.stdin.readline().split()))


n = Ii()
num = 10
mod = 10**9 + 7
ans = (pow(num, n, mod) - pow(num - 1, n, mod) - pow(num - 1, n, mod) + pow(num - 2, n, mod)) % mod
print(ans)
