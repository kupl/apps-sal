mod = 998244353
maxn = 1005
'''
def q_mod(a,b):
    ans = 1
    a %= mod
    while b != 0:
        if b&1 == 1:
            ans = ans * a % mod
            b -= 1
        b >>= 1
        a = a * a % mod
    return ans

def C(n,m):
    if m >n :
        return 0
    ans = 1
    for i in range(1,m+1):
        a = (n + i - m) % mod
        b = i % mod
        ans = ans * (a * q_mod(b , mod-2) % mod ) % mod
    return ans 

def Lucas(n,m):
    if m == 0:
        return 1
    return  C(n % mod,m % mod) * Lucas(int(n/mod) , int(m/mod)) % mod
'''
'''
C = [ ([0]*maxn) for i in range(maxn)]

for i in range(2,maxn):
    for j in range(i+1):
        if j == 0 or j == i:
            C[i][j] = 1
            continue;
        C[i][j] = (C[i-1][j] + C[i-1][j-1]) % mod


def A(n,m):
    j = 0
    ans = 1
    for i in range(0,n+1):
        if j == m:
            break
        j += 1
        ans = (ans * (n - i)) % mod
    return ans

'''


def solve(n, m):
    if n > m:
        n, m = m, n
    ans, s = 0, 1
    for i in range(0, n + 1):
        ans = ans + s
        s = s * (n - i) // (i + 1) * (m - i)
    return ans


while True:
    try:
        a, b, c = list(map(int, input().split()))
        print(solve(a, b) * solve(a, c) * solve(b, c) % mod)
    except:
        break
