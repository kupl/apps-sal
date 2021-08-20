"""
n, m = map(int, input().split())
a = input()
b = input()
b_ind = []
mo = 998244353
ans = 0

b_ind.append(int(b[0]))
for i in range(1, m):
	b_ind.append(b_ind[i-1]+int(b[i]))

for i in range(1, n+1):
	if a[-i] == '1' and i<=m:
		ans += (pow(2, i-1, mo)*b_ind[-i])%mo

print(ans%mo)

"""
(n, m) = list(map(int, input().split()))
a = input()
b = input()
b_ind = []
mo = 998244353
ans = 0
b_ind.append(int(b[0]))
for i in range(1, m):
    b_ind.append(b_ind[i - 1] + int(b[i]))
for i in range(1, n + 1):
    if a[-i] == '1' and i <= m:
        ans += pow(2, i - 1, mo) * b_ind[-i] % mo
print(ans % mo)
