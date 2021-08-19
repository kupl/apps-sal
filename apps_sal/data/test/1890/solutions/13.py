s = input()
k = int(input())

p = 10**9 + 7
n = len(s)
amodp = (pow(2, k * n, p) - 1) % p

b1modp = pow((2**n) - 1, p - 2, p)

MOD = (amodp * b1modp) % p
ans = 0
for i in range(len(s)):
    if(s[i] == '5' or s[i] == '0'):
        ans += pow(2, i, 10**9 + 7)
Ans = 0

Ans += ans * (MOD)

Ans %= p
# for i in range(k):
# Ans+=ans*pow(2,i*len(s),10**9+7)

print(Ans)


##x^k - 1
# ---------
##x  - 1
##
##
##x = 2**n
##
##2^kn - 1
# ---------
##2^n - 1
##
##amodp = (pow(2,k*n,p)-1)%p
##
##b1modp = pow ( 2**k-1 , p-2 , p )
##
##MOD = (amodp*b1modp) % p
##
##
##
# (a / b) mod p = ((a mod p) * (b^(-1) mod p)) mod p
##
# b^(-1) mod p = b^(p - 2) mod p
