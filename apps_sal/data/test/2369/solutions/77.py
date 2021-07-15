N, K = list(map(int, input().split()))
A = [int(i) for i in input().split()]
mod = 10**9 + 7

list_size = 10**5 + 1
 
f_list = [1] * list_size
f_r_list = [1] * list_size
 
for i in range(list_size-1):
	f_list[i+1] = (f_list[i] * (i+1)) % mod
 
f_r_list[-1] = pow(f_list[-1], mod - 2, mod)
 
for i in range(list_size-2, -1, -1):
	f_r_list[i] = (f_r_list[i+1] * (i+1)) % mod
 
def comb(n, r, mod):
	if n < r or r < 0:
		return 0
	elif n == 0 or r == 0 or n == r:
		return 1
	else:
		return (f_list[n] * f_r_list[n-r] * f_r_list[r]) % mod

A.sort()
ans = 0
for i, a in enumerate(A, start=1):
    if i <= N-K+1:
        ans -= (a * comb(N-i, K-1, mod))%mod
ans %= mod

A.sort(reverse=True)

for i, a in enumerate(A, start=1):
    if i <= N-K+1:
        ans += (a * comb(N-i, K-1, mod))%mod
ans %= mod
print(ans)

