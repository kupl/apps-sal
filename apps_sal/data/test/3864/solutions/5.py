N = int(input())
MOD = 998244353

arr = [(pow(2,N-1,MOD) * N) % MOD] * 2
b,a = 2,3
while len(arr) <= N//2:
    arr.append((arr[-1] + b*a)%MOD)
    b *= 4
    b %= MOD
    a += 2

inv = pow(2,-N,MOD)
if N <= 2:
    for a in arr[:N]:
        print((a * inv) % MOD)
    return

if N%2==0: arr.pop()

for a in arr:
    print((a * inv) % MOD)

if N%2: arr.pop()
for a in arr[::-1]:
    print((a * inv) % MOD)
