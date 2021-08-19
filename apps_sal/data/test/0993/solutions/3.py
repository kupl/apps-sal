from collections import Counter
(n, m) = map(int, input().split())
a = list(map(int, input().split()))
tmp = 0
ca = [tmp]
for ai in a:
    tmp += ai
    tmp %= m
    ca.append(tmp)
cnt_ca = Counter(ca)
ans = 0
for c in cnt_ca.values():
    ans += c * (c - 1) // 2
print(ans)
