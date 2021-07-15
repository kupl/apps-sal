n = int(input())
mod = 10**9+7
if n <= 1:
    print((0))
    return
print(((pow(10, n, mod)-2*pow(9, n, mod)+pow(8, n, mod)) % mod))

