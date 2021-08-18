
S = input().strip()
num = 0
cnt_mod = {0: 1}
mod = 2019
base_pow = 1

for i in range(len(S)):
    digit = int(S[len(S) - 1 - i])

    num += (digit * base_pow) % mod
    num %= mod

    base_pow = (base_pow * 10) % mod

    cnt_mod.setdefault(num, 0)
    cnt_mod[num] += 1


ans = 0

for r, c in list(cnt_mod.items()):
    if c >= 2:
        ans += c * (c - 1) // 2

print(ans)
