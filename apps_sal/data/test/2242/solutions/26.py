S = input()

mod = 2019
cnt = [0] * 2019
cur = 0  # 現在検討中の部分文字列
cnt[cur] = 1
d = 1   # 桁

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
