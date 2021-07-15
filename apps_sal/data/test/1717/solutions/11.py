N = int(input())

#1～Nまでの最小公倍数+1が答え

#最小公約数を求める

def gcd(a, b) :
    while b != 0:
        a, b = b, a%b
    return a

#最小公倍数

def lcm(a, b) :
    return int(a*b/gcd(a,b))

ans = 2

for i in range(3,N+1):
    ans = lcm(ans,i)

print((ans+1))

