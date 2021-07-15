import sys

readline = sys.stdin.readline
readlines = sys.stdin.readlines
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')

n_ = 5 * 10**5 + 10
mod = 998244353
fun = [1] * (n_ + 1)
for i in range(1, n_ + 1):
    fun[i] = fun[i - 1] * i % mod
rev = [1] * (n_ + 1)
rev[n_] = pow(fun[n_], mod - 2, mod)
for i in range(n_ - 1, 0, -1):
    rev[i] = rev[i + 1] * (i + 1) % mod

def nCr(n, r):
    if r > n:
        return 0
    return fun[n] * rev[r] % mod * rev[n - r] % mod

def solve():
    n, k = nm()
    res = 0
    for i in range(1, n+1):
        if i * k > n:
            break
        res = (res + nCr(n//i-1, k-1)) % mod
    print(res)
    return


solve()

# T = ni()
# for _ in range(T):
#     solve()

