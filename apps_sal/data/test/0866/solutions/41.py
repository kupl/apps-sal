x,y = list(map(int, input().split()))

if (x+y) % 3 != 0:
    print(0)
    return

a = (2*x - y) // 3
b = (2*y - x) // 3

if a < 0 or b < 0:
    # (x,y) = (1,5)とかは無理
    print(0)
    return
    
MOD = 10**9+7
def fact(x):
    f = 1
    for i in range(2, x+1):
        f *= i
        f %= MOD
    return f

def fact_inv(x):
    return pow(fact(x), MOD-2, MOD)

ans = fact(a+b) * fact_inv(a) * fact_inv(b) % MOD

print(ans)
