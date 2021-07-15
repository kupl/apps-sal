import math

mod = 10**9+7
N,M,K = list(map(int, input().split()))
MAX = min(N*M,mod)

facts = [1 for i in range(MAX)]
invs = [1 for i in range(MAX)]

def inv(x):
	return pow(x,mod-2,mod)

for i in range(1,MAX):
    facts[i] = (facts[i-1] * i)% mod
    invs[i] = inv(facts[i])

def nCr(n,r):
	return facts[n] * invs[r] * invs[n-r] % mod

def main():
    ans = 0
    complement = nCr((N*M-2)%mod,(K-2)%mod)
    for i in range(1,N):
        ans += i * (N-i) * M**2
    for i in range(1,M):
        ans += i * (M-i) * N**2
    print(((ans*complement) % mod))

main()

