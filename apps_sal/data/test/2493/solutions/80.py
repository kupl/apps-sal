n = int(input())
a = list(map(int, input().split()))

mod = 10 ** 9 + 7
N = 100000

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
    if n < r or n < 0 or r < 0:
        return 0
    else:
        return kai[n] * rev_kai[r] * rev_kai[n-r] % mod

d = {}

# n1個 X n2個 X n3個
n1 = 0
n2 = 0
n3 = 0

for i, ai in enumerate(a):
    if ai not in d:
        d[ai] = i
    else:
        n1 = d[ai]
        n2 = i - d[ai] - 1
        n3 = n - i
        break

for i in range(1, n+2):
    ans = 0
    # Xを選ばない
    ans += cmb(n-1, i)
    # Xを2回選ぶ
    ans += cmb(n-1, i-2)
    # Xを1回選ぶ かつ Xの間からは選ばない
    ans += cmb(n-1-n2, i-1)
    # Xを1回選ぶ かつ Xの間から一つ以上選ぶ
    if i >= 2 and i <= n:
        ans += 2 * (cmb(n2+n1+n3, i-1) - cmb(n1+n3, i-1))

    print((ans % mod))

