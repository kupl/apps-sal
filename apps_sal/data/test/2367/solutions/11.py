h, w, a, b = map(int, input().split())

n = 2 * 10 ** 5
k = 2 * 10 ** 5
mod = 10**9 + 7

modinv_table = [-1] * (k+1)
modinv_table[1] = 1
for i in range(2, k+1):
    modinv_table[i] = (-modinv_table[mod % i] * (mod // i)) % mod

def prepare_binomial_coefficients(n, k):
    for i in range(1,n+1):
        bc_num[i] = i * bc_num[i-1] % mod
    bc_num[0] = 0
    for i in range(1,k+1):
        bc_den[i] = modinv_table[i] * bc_den[i-1] % mod
    return

def binomial_coefficients(n, k):
    if n == 0 and k == 0:
        return 1
    return bc_num[n] * bc_den[k] * bc_den[n-k] % mod

bc_num = [1]*(n+1)
bc_den = [1]*(n+1)
prepare_binomial_coefficients(n, n)

mids = [0]*(w-b)
dis_mid = h - a - 1
for i in range(w-b):
    mids[i] = binomial_coefficients(dis_mid+i+b,i+b)

#print(mids)

mids_down = [0]*(w-b)
dis_mid = a
for i in range(w-b):
    mids_down[i] = binomial_coefficients(dis_mid+w-b-i-1,w-b-i-1)

#print(mids_down)

for i in range(w-b-1):
    mids_down[i] -= mids_down[i+1]

#print(mids_down)

for i in range(w-b):
    mids[i] = (mids[i] * mids_down[i]) % mod

#print(mids)

print(sum(mids)%mod)
