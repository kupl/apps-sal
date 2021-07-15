Mod = 1000000000 + 7

def fastpow(x,y):
    ans = 1

    nonlocal Mod
    while y:
        if (y & 1): ans = (ans * x) % Mod
        x = (x * x) % Mod
        y >>= 1
    return ans

def solve(N,K):
    # f[i] is number (x1,....xn) such that gcd(x1,..,xK) = i
    
    f = [0]*(K + 1)
    for i in range(K,0,-1):
        f[i] = fastpow(K//i,N)
        for j in range(i + i,K + 1,i):
            f[i] -= f[j]

    nonlocal Mod
    ans = 0
    for i in range(1,K + 1):
        ans = (ans + i*f[i]) % Mod
    return ans


def __starting_point():
    
    N, K = list(map(int,input().split()))
    print((solve(N,K)))

__starting_point()
