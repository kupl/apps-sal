import sys
def factorial():
    nonlocal mod
    fac = [1] * int(3e5 + 1)
    for i in range(1, int(3e5)):
        fac[i] = i*fac[i-1] % mod
    return fac
def inverse(x):
    nonlocal mod
    return pow(x, mod-2, mod)
def C(n, r):
    nonlocal fac
    if n < 0 or n < r:
        return 0
    return fac[n]*inverse(fac[r])*inverse(fac[n-r]) % mod
def calc(f, w, h):
    nonlocal mod
    if w == 0:
        return 1
    ans = 0
    for k in range(1, min(w//(h+1),f+1)+1):
        ans += C(f+1, k) * C(w-k*h-1, k-1) % mod
        ans %= mod
    return ans
f, w, h = list(map(int,sys.stdin.readline().split(' ')))
mod = int(1e9 + 7)
fac = factorial()
cnt = calc(f, w, h)
sys.stdout.write(str(cnt*inverse(C(f+w, w)) % mod))


