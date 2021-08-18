S = input()

mod = 2019
cnt = [0] * 2019
cur = 0
cnt[cur] = 1
d = 1

for s in S[::-1]:
    cur += int(s) * d
    cur %= mod
    cnt[cur] += 1
    d *= 10
    d %= mod

ans = 0
for c in cnt:
    ans += c * (c - 1) // 2

print(ans)
