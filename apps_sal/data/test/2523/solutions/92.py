# 初めは0と1で多い方だと思った
# 正確にやってはないけど連続する0or1より長くないとだめ
# 上限が何かを考える
s = input()
l = len(s)

ans = 1000000000000
for i in range(l - 1):
    if s[i] != s[i + 1]:
        ne = max(i + 1, l - i - 1)
        ans = min(ans, ne)
if ans == 1000000000000:
    print(l)
else:
    print(ans)
