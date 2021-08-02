N = 10**6
mod = 10**9 + 7


def checkgood(val, a, b):
    while(val):
        if(val % 10 != a and val % 10 != b):
            return False
        val //= 10
    return(True)


def power(x, a):
    if(a == 0):
        return(1)
    z = power(x, a // 2)
    z = (z**2) % mod
    if(a % 2):
        z = (z * x) % mod
    return(z)


fact = [1 for _ in range(N + 1)]
for no in range(2, N + 1):
    fact[no] = (fact[no - 1] * no) % mod
[a, b, n] = list(map(int, input().split()))
count = 0
for freq in range(n + 1):
    val = freq * a + (n - freq) * b
    if(checkgood(val, a, b)):
        count += (((fact[n] * power(fact[freq], mod - 2)) % mod) * power(fact[n - freq], mod - 2)) % mod
        count %= mod
print(count)
