#f_listとf_r_listの要素数は状況に応じて変えよう

MOD = 10**9 + 7
list_size = 2000003

f_list = [1] * list_size
f_r_list = [1] * list_size

for i in range(list_size - 1):
	f_list[i + 1] = int((f_list[i] * (i + 2)) % MOD)

f_r_list[-1] = pow(f_list[-1], MOD - 2, MOD)

for i in range(2, list_size + 1):
	f_r_list[-i] = int((f_r_list[-i + 1] * (list_size + 2 - i)) % MOD)

def comb(n, r):
	if n < r:
		return 0
	elif n == 0 or r == 0 or n == r:
		return 1
	else:
		return (((f_list[n - 1] * f_r_list[n - r - 1]) % MOD) * f_r_list[r - 1]) % MOD 

def f(x, y):
	if x * y == 0:
		return 0
	elif x == 1:
		return y * (y+3) // 2
	else:
		return comb(x+y+2, x+1) - x - y - 2


r1, c1, r2, c2 = list(map(int, input().split()))
ans = (f(r2, c2) + f(r1-1, c1-1) - f(r1-1, c2) - f(r2, c1-1)) % MOD
print(ans)
