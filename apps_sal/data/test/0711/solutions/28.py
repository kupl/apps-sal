n, m = map(int, input().split())

mod = 10 ** 9 + 7
N = 200000

#逆元テーブル
inv_t = [0]+[1]
for i in range(2, N):
  inv_t += [inv_t[mod % i] * (mod - int(mod / i)) % mod]

#階乗計算
kai = [1, 1]
rev_kai = [1, inv_t[1]]
for i in range(2, N):
	kai.append(kai[-1] * i % mod)
	rev_kai.append(rev_kai[-1] * inv_t[i] % mod)

# コンビネーション計算
def cmb(n, r):
	return kai[n] * rev_kai[r] * rev_kai[n-r] % mod

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

ans = 1

for _, cnt in factorization(m):
    if _ == 1:
        break
    ans = ans * cmb(cnt + n - 1, n - 1) % mod

print(ans)
