MOD = 10 ** 9 + 7
MOD1 = 2 * (10 ** 9 + 6)

pow2 = [0] * 32 #pow2[i] = 2 ** (2 ** i) % MOD
pow2[0] = 2
for i in range(1, 32):
    pow2[i] = (pow2[i - 1] ** 2) % MOD

def exp2mod(exp):
    ans = 1
    the_pow = 1
    the_log = 0
    while the_pow <= exp:
        if exp & the_pow == the_pow:
            ans = (ans * pow2[the_log]) % MOD
        the_pow *= 2
        the_log += 1
    return ans

def main():
    n = 1
    k = int(input())
    a = input().split()
    x = 0
    y = 0
    for i in range(k):
        n = (n * int(a[i])) % MOD1
    
    x = exp2mod(n)
    if n % 2 == 0:
        x = (x + 2) % MOD
    else:
        x = (x - 2) % MOD
    if x % 2 == 0:
        x = x // 2
    else:
        x = (x + MOD) // 2
    if x % 3 == 0:
        x = x // 3
    elif x % 3 == 1:
        x = (x + MOD) // 3
    else:
        x = (x + 2 * MOD) // 3
        
    y = exp2mod(n)
    if y % 2 == 0:
        y = y // 2
    else:
        y = (y + MOD) // 2
    
    print(str(x) + "/" + str(y))
        
main()

