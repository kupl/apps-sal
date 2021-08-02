l = str(input())
ll = len(l)
mod = 10**9 + 7

ans = 0
t1 = 0
for i in range(ll):
    if l[i] == "0":
        continue
    ans = (ans + pow(2, t1, mod) * pow(3, ll - i - 1, mod) % mod) % mod
    t1 += 1

ans = (ans + pow(2, t1, mod)) % mod

print(ans)
